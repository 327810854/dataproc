# dataproc

Project structure

dataproc/
 ├── video/
 │    ├── video_tools.py
 │    └── __init__.py
 ├── image/
 ├── data/
 ├── examples/
 │    ├── sample.mp4
 │    └── output_demo.mp4
 ├── tests/
 │    └── test_video.py
 ├── README.md
 └── requirements.txt

# dataproc

Dataproc is a lightweight Python data & media processing toolkit developed for the AI Practice (OSS) course.
The project follows Git/GitHub workflows including branching, issue tracking, pull requests, and collaborative development.
This repository contains multiple functional modules, including video processing, image tools, and additional data utilities.

## Features (current status)

Video Processing Module (Jdz1128)

Provides essential video editing utilities such as:

Cut video clips

Resize videos (scale factor or resolution)

Convert to grayscale

Change playback speed

Add watermark (image/text)

All functions are implemented using Python and MoviePy.

## Installation

git clone https://github.com/327810854/dataproc.git
cd dataproc
pip install -r requirements.txt



## Usage: Image preprocessing

Import the module
      from video.video_tools import (
    cut_clip,
    resize_video,
    resize_to_resolution,
    to_grayscale,
    change_speed,
    add_watermark,
      )

1) Cut a video clip
Function:
cut_clip(input_path, output_path, start, end)

Parameters:
input_path: input video file
output_path: output file
start: start time (seconds)
end: end time (seconds)

Example
cut_clip("sample.mp4", "clip.mp4", start=3, end=10)

2) Resize a video by scale factor
Function:
resize_video(input_path, output_path, factor)

Example:
resize_video("sample.mp4", "small.mp4", factor=0.5)

3) Resize to specific resolution
Function:
resize_to_resolution(input_path, output_path, width, height)

Example:
resize_to_resolution("sample.mp4", "1080p.mp4", 1920, 1080)

4) Convert to grayscale
Function:
to_grayscale(input_path, output_path)

Example:
to_grayscale("sample.mp4", "gray.mp4")

5) Change playback speed
Function:
change_speed(input_path, output_path, factor)

Example:
change_speed("sample.mp4", "fast.mp4", factor=2.0)   # 2x faster
change_speed("sample.mp4", "slow.mp4", factor=0.5)   # 0.5x slower

6) Add watermark (image or text)
Function:
add_watermark(input_path, output_path, watermark_path, pos=("right","bottom"))

Example:
add_watermark(
    "sample.mp4",
    "wm.mp4",
    watermark_path="logo.png",
    pos=("right", "bottom")
)

## Development workflow (for contributors)

We follow a simple GitHub workflow:

- Create an issue for a new feature or bug.
- Create a feature branch from `main`.
- Commit changes to the feature branch with clear commit messages.
- Push the branch to GitHub.
- Open a Pull Request (PR) and link it to the issue.
- After review, merge the PR into `main` and close the issue.

---