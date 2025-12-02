"""
Image preprocessing submodule for dataproc.

Usage example:

from dataproc.images import preprocess

preprocess.resize_image("input.jpg", "output.jpg", (256, 256))
"""

from .preprocess import (
    open_image,
    save_image,
    resize_image,
    to_grayscale,
    rotate_image,
    blur_image,
)