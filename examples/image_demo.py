from pathlib import Path
from PIL import Image
from dataproc.images import preprocess as prep

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
INPUT_PATH = BASE_DIR / "input.jpg"

def ensure_input_image(path: Path) -> None:
    if path.exists():
        return
    Image.new("RGB", (512, 512), color=(255, 0, 0)).save(path, format="JPEG")

def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ensure_input_image(INPUT_PATH)
    prep.resize_image(INPUT_PATH, OUTPUT_DIR / "resized_256x256.jpg", (256, 256))
    prep.to_grayscale(INPUT_PATH, OUTPUT_DIR / "gray.jpg")
    prep.rotate_image(INPUT_PATH, OUTPUT_DIR / "rotated_45.jpg", 45)
    prep.blur_image(INPUT_PATH, OUTPUT_DIR / "blurred.jpg", 2.0)
    print("demo done: outputs saved to", OUTPUT_DIR)

if __name__ == "__main__":
    main()
