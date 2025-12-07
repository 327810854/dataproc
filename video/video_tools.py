from moviepy import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.fx import BlackAndWhite, MultiplySpeed
# 剪切视频 cut
def cut_clip(input_path, output_path, start_time, end_time):
    clip = VideoFileClip(input_path).subclipped(start_time, end_time)
    clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        ffmpeg_params=["-pix_fmt", "yuv420p"],
    )
    clip.close()

# 缩放视频  resize
def resize_video(input_path, output_path, scale=0.5):
    clip = VideoFileClip(input_path)

    orig_w, orig_h = clip.w, clip.h
    new_w = int(orig_w * scale)
    new_h = int(orig_h * scale)


    if new_w % 2 == 1:
        new_w -= 1
    if new_h % 2 == 1:
        new_h -= 1

    new_clip = clip.resized(new_size=(new_w, new_h))


    new_clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        ffmpeg_params=["-pix_fmt", "yuv420p"],
    )

    clip.close()
    new_clip.close()

def resize_to_resolution(input_path, output_path, target_w, target_h):
    clip = VideoFileClip(input_path)

    orig_w, orig_h = clip.w, clip.h
    scale_w = target_w / orig_w
    scale_h = target_h / orig_h
    scale = min(scale_w, scale_h)

    new_w = int(orig_w * scale)
    new_h = int(orig_h * scale)


    if new_w % 2 == 1:
        new_w -= 1
    if new_h % 2 == 1:
        new_h -= 1

    new_clip = clip.resized(new_size=(new_w, new_h))


    new_clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        ffmpeg_params=["-pix_fmt", "yuv420p"],
    )

    clip.close()
    new_clip.close()
# 变成黑白   black white
def to_grayscale(input_path, output_path):
    clip = VideoFileClip(input_path)
    gray_clip = clip.with_effects([BlackAndWhite()])
    gray_clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        ffmpeg_params=["-pix_fmt", "yuv420p"],
    )
    clip.close()
    gray_clip.close()

# 改变速度 speed
def change_speed(input_path, output_path, factor):
    clip = VideoFileClip(input_path)
    speed_clip = clip.with_effects([MultiplySpeed(factor=factor)])
    speed_clip.write_videofile(
        output_path,
        codec="libx264",
        audio_codec="aac",
        ffmpeg_params=["-pix_fmt", "yuv420p"],
    )
    clip.close()
    speed_clip.close()