"""
Simple demo for the image preprocessing module.

Run this script from the project root:

    python -m examples.image_demo
"""

from pathlib import Path
from PIL import Image
from dataproc.images import preprocess


BASE_DIR = Path(__file__).resolve().parent
INPUT_IMAGE = BASE_DIR / "input.jpg"
OUTPUT_DIR = BASE_DIR / "output"


def _ensure_input_image() -> None:
    """Create a simple test image if examples/input.jpg does not exist."""
    if INPUT_IMAGE.exists():
        return
    img = Image.new("RGB", (320, 240), (200, 220, 255))
    preprocess.save_image(img, INPUT_IMAGE)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    _ensure_input_image()

    # 1. Resize
    resize_out = OUTPUT_DIR / "resized_256x256.jpg"
    preprocess.resize_image(INPUT_IMAGE, resize_out, (256, 256))
    print(f"Saved resized image to {resize_out}")

    # 2. Grayscale
    gray_out = OUTPUT_DIR / "gray.jpg"
    preprocess.to_grayscale(INPUT_IMAGE, gray_out)
    print(f"Saved grayscale image to {gray_out}")

    # 3. Rotate
    rotated_out = OUTPUT_DIR / "rotated_45.jpg"
    preprocess.rotate_image(INPUT_IMAGE, rotated_out, angle=45)
    print(f"Saved rotated image to {rotated_out}")

    # 4. Blur
    blurred_out = OUTPUT_DIR / "blurred.jpg"
    preprocess.blur_image(INPUT_IMAGE, blurred_out, radius=3.0)
    print(f"Saved blurred image to {blurred_out}")


if __name__ == "__main__":
    main()