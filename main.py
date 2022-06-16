import os

import pydub
import pyrubberband
import soundfile as sf
import yt_dlp
from moviepy.editor import VideoFileClip, AudioFileClip
from tkinter import *


def get_original_video(video_info, folder):
    if os.path.exists(f"{folder}/{video_info['title']}.mp4"):
        os.remove(f"{folder}/{video_info['title']}.mp4")
    options = {
        'format': '137+140',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'outtmpl': f"{folder}{video_info['title']}.mp4",
        'keepvideo': True,
        'keepaudio': True,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])


def pitch_shift(folder, title, step):
    audio = folder + title + '.f140.m4a'
    sound = pydub.AudioSegment.from_file(audio)
    sound.export('out.wav', format='wav')
    y, sr = sf.read('out.wav')
    y_shift = pyrubberband.pitch_shift(y, sr=sr, n_steps=step)
    sf.write('outshifted.wav', y_shift, sr, format="wav")

    os.remove(folder + title + '.f140.m4a')
    os.remove('out.wav')


def scale_changed_video(folder, title, scale):
    video = VideoFileClip(folder + title + '.f137.mp4')
    audio = AudioFileClip('outshifted.wav')

    videoclip = video.set_audio(audio)
    videoclip.write_videofile(folder + title + f'_scale_changed_{int(scale)}.mp4')

    os.remove(folder + title + '.f137.mp4')
    os.remove('outshifted.wav')


def main(root, url, scale=0, output_folder='~'):
    info = yt_dlp.YoutubeDL().extract_info(
        url=url, download=False
    )
    get_original_video(info, output_folder)
    if scale:
        pitch_shift(output_folder, info['title'], int(scale))
        scale_changed_video(output_folder, info['title'], scale)

    Label(root, text=f"Download Complete!!! Videos stored to {output_folder}").place(anchor=CENTER, relx=.5, rely=.8)
