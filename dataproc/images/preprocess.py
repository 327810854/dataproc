"""
dataproc.images.preprocess

This module contains basic image preprocessing functions, such as:

- opening and saving images
- resizing
- converting to grayscale
- rotating
- applying simple blur

We use the Pillow library (PIL) for image processing.
"""

from pathlib import Path
from typing import Tuple, Union

from PIL import Image, ImageFilter

PathLike = Union[str, Path]


def open_image(path: PathLike) -> Image.Image:
    """
    Open an image file and return a Pillow Image object.

    Parameters
    ----------
    path : str or Path
        Path to the image file.

    Returns
    -------
    Image.Image
        The loaded image.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Image file not found: {path}")
    return Image.open(path)


def save_image(img: Image.Image, path: PathLike) -> None:
    """
    Save a Pillow Image object to a file.

    Parameters
    ----------
    img : Image.Image
        The image to save.
    path : str or Path
        Output path. The format is inferred from the file extension.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def resize_image(
    input_path: PathLike,
    output_path: PathLike,
    size: Tuple[int, int],
) -> None:
    """
    Resize an image to the given size and save to output_path.

    Parameters
    ----------
    input_path : str or Path
        Path to the input image.
    output_path : str or Path
        Path to save the resized image.
    size : (int, int)
        (width, height) in pixels.
    """
    img = open_image(input_path)
    resized = img.resize(size)
    save_image(resized, output_path)


def to_grayscale(
    input_path: PathLike,
    output_path: PathLike,
) -> None:
    """
    Convert an image to grayscale and save to output_path.
    """
    img = open_image(input_path)
    gray = img.convert("L")  # "L" mode = grayscale
    save_image(gray, output_path)


def rotate_image(
    input_path: PathLike,
    output_path: PathLike,
    angle: float,
    expand: bool = True,
) -> None:
    """
    Rotate an image by the given angle and save to output_path.

    Parameters
    ----------
    input_path : str or Path
        Path to the input image.
    output_path : str or Path
        Path to save the rotated image.
    angle : float
        Rotation angle in degrees. Positive values rotate counter-clockwise.
    expand : bool, default True
        If True, expand the output image to hold the entire rotated image.
    """
    img = open_image(input_path)
    rotated = img.rotate(angle, expand=expand)
    save_image(rotated, output_path)


def blur_image(
    input_path: PathLike,
    output_path: PathLike,
    radius: float = 2.0,
) -> None:
    """
    Apply a simple Gaussian blur to an image and save to output_path.

    Parameters
    ----------
    input_path : str or Path
        Path to the input image.
    output_path : str or Path
        Path to save the blurred image.
    radius : float, default 2.0
        Blur radius for the Gaussian blur filter.
    """
    img = open_image(input_path)
    blurred = img.filter(ImageFilter.GaussianBlur(radius=radius))
    save_image(blurred, output_path)