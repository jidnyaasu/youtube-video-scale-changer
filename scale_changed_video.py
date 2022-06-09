import os
from moviepy.editor import VideoFileClip, AudioFileClip


def scale_changed_video(folder, title, scale):
    video = VideoFileClip(folder + title + '.f137.mp4')
    audio = AudioFileClip('outshifted.wav')

    videoclip = video.set_audio(audio)
    videoclip.write_videofile(folder + title + f'_scale_changed_{int(scale)}.mp4')

    os.remove(folder + title + '.f137.mp4')
    os.remove('outshifted.wav')
