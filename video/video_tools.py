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
