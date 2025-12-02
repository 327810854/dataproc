# dataproc

Project structure

dataproc/
├── dataproc/
│   ├── __init__.py
│   └── images/
│       ├── __init__.py
│       └── preprocess.py
├── examples/
│   └── image_demo.py
├── requirements.txt
└── README.md
# dataproc

An open-source data preprocessing library for different types of data, such as images, text, audio, and more. This project is part of a course assignment and is intended to practice open-source collaboration on GitHub.

## Features (current status)

- **Images**
  - Open and save images
  - Resize images
  - Convert images to grayscale
  - Rotate images by a given angle
  - Apply a simple Gaussian blur

> Other data types (text, audio, video, etc.) can be added by other teammates.

## Installation

It is recommended to use Python 3.10+.

1. Clone the repository:

```bash
git clone https://github.com/327810854/dataproc.git
cd dataproc
```

2. Create and activate a virtual environment (Windows):

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage: Image preprocessing

Here is a simple example of how to use the image preprocessing utilities:

```python
from dataproc.images import preprocess

# Resize an image
preprocess.resize_image("input.jpg", "output_resized.jpg", (256, 256))

# Convert to grayscale
preprocess.to_grayscale("input.jpg", "output_gray.jpg")

# Rotate an image by 45 degrees
preprocess.rotate_image("input.jpg", "output_rotated.jpg", angle=45)

# Apply a blur effect
preprocess.blur_image("input.jpg", "output_blur.jpg", radius=3.0)
```

You can also run the example script:

```bash
python -m examples.image_demo
```

This will generate several processed images under `examples/output`.

## Development workflow (for contributors)

We follow a simple GitHub workflow:

- Create an issue for a new feature or bug.
- Create a feature branch from `main`.
- Commit changes to the feature branch with clear commit messages.
- Push the branch to GitHub.
- Open a Pull Request (PR) and link it to the issue.
- After review, merge the PR into `main` and close the issue.

---