import os
from moviepy.editor import VideoFileClip, AudioFileClip


def scale_changed_video(folder, title, scale):
    video = VideoFileClip('out.mp4')
    audio = AudioFileClip('outshift.wav')

    videoclip = video.set_audio(audio)

    videoclip.write_videofile(folder + title + f'_scale_changed_{int(scale)}.mp4')
    os.remove('out.mp4')
    os.remove('outshift.wav')
