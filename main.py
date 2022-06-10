import os

import librosa
import soundfile as sf
import yt_dlp
from moviepy.editor import VideoFileClip, AudioFileClip


def get_original_video(video_info, folder):
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
    y, sr = librosa.load(folder + title + '.f140.m4a')

    y_shift = librosa.effects.pitch_shift(y, sr=sr, n_steps=step)
    sf.write('outshifted.wav', y_shift, sr, format="wav")

    os.remove(folder + title + '.f140.m4a')


def scale_changed_video(folder, title, scale):
    video = VideoFileClip(folder + title + '.f137.mp4')
    audio = AudioFileClip('outshifted.wav')

    videoclip = video.set_audio(audio)
    videoclip.write_videofile(folder + title + f'_scale_changed_{int(scale)}.mp4')

    os.remove(folder + title + '.f137.mp4')
    os.remove('outshifted.wav')


def main(url, scale=0, output_folder='~'):
    info = yt_dlp.YoutubeDL().extract_info(
        url=url, download=False
    )
    get_original_video(info, output_folder)
    if scale:
        pitch_shift(output_folder, info['title'], int(scale))
        scale_changed_video(output_folder, info['title'], scale)

    return "Download complete!"
