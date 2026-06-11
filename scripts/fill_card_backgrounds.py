from collections import deque
from pathlib import Path
import re
from statistics import median

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
REVIEW_HTML = ROOT / "outputs/national-parks-poker/index.html"
SOURCE_DIR = ROOT / "outputs/national-parks-poker/digital/cards"
OUTPUT_DIR = ROOT / "outputs/national-parks-poker/digital/cards-filled"
CARD_BACK_SOURCE = ROOT / "outputs/national-parks-poker/digital/card-back-v2.png"
CARD_BACK_OUTPUT = ROOT / "outputs/national-parks-poker/digital/card-back-v2-filled.png"

DARK_THRESHOLD = 80


def active_card_files():
    html = REVIEW_HTML.read_text(encoding="utf-8")
    files = re.findall(r'file: "([^"]+\.png)"', html)
    if len(files) != 54:
        raise RuntimeError(f"Expected 54 active card references, found {len(files)}")
    if len(set(files)) != 54:
        raise RuntimeError("Expected 54 unique active card references")
    return files


def is_dark(pixel):
    red, green, blue, alpha = pixel
    return alpha > 0 and red <= DARK_THRESHOLD and green <= DARK_THRESHOLD and blue <= DARK_THRESHOLD


def is_paper_candidate(pixel):
    red, green, blue, alpha = pixel
    if alpha == 0:
        return False
    if red <= 170 or green <= 145 or blue <= 110:
        return False
    return max(red, green, blue) - min(red, green, blue) < 100


def sample_fill_color(image):
    width, height = image.size
    pixels = image.load()
    samples = []

    x_start = min(40, width)
    x_end = max(width - 40, x_start)
    y_start = min(40, height)
    y_end = max(height - 40, y_start)

    top_bottom_bands = list(range(y_start, min(130, height))) + list(range(max(height - 130, 0), y_end))
    for y in top_bottom_bands:
        for x in range(x_start, x_end):
            pixel = pixels[x, y]
            if is_paper_candidate(pixel):
                samples.append(pixel[:3])

    left_right_bands = list(range(x_start, min(130, width))) + list(range(max(width - 130, 0), x_end))
    for x in left_right_bands:
        for y in range(y_start, y_end):
            pixel = pixels[x, y]
            if is_paper_candidate(pixel):
                samples.append(pixel[:3])

    if not samples:
        return (242, 227, 195, 255)

    return tuple(int(median(sample[channel] for sample in samples)) for channel in range(3)) + (255,)


def fill_border_connected_dark_pixels(source_path, output_path):
    image = Image.open(source_path).convert("RGBA")
    width, height = image.size
    pixels = image.load()
    fill_color = sample_fill_color(image)

    queue = deque()
    seen = set()

    def enqueue_if_dark(x, y):
        point = (x, y)
        if point not in seen and is_dark(pixels[x, y]):
            seen.add(point)
            queue.append(point)

    for x in range(width):
        enqueue_if_dark(x, 0)
        enqueue_if_dark(x, height - 1)

    for y in range(height):
        enqueue_if_dark(0, y)
        enqueue_if_dark(width - 1, y)

    while queue:
        x, y = queue.popleft()
        pixels[x, y] = fill_color
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < width and 0 <= ny < height:
                enqueue_if_dark(nx, ny)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)
    return {
        "file": source_path.name,
        "size": f"{width}x{height}",
        "fill_color": fill_color[:3],
        "pixels_replaced": len(seen),
    }


def main():
    results = []
    for filename in active_card_files():
        source_path = SOURCE_DIR / filename
        if not source_path.exists():
            raise FileNotFoundError(source_path)
        results.append(fill_border_connected_dark_pixels(source_path, OUTPUT_DIR / filename))

    print(f"Wrote {len(results)} filled cards to {OUTPUT_DIR}")
    for result in results:
        print(
            f"{result['file']}: {result['size']}, "
            f"fill={result['fill_color']}, replaced={result['pixels_replaced']}"
        )

    card_back_result = fill_border_connected_dark_pixels(CARD_BACK_SOURCE, CARD_BACK_OUTPUT)
    print(
        f"Wrote filled card back to {CARD_BACK_OUTPUT}: "
        f"{card_back_result['size']}, fill={card_back_result['fill_color']}, "
        f"replaced={card_back_result['pixels_replaced']}"
    )


if __name__ == "__main__":
    main()
