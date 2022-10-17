import os

import pydub
import pyrubberband
import soundfile as sf
import yt_dlp
from moviepy.editor import VideoFileClip, AudioFileClip


def get_original_video(label, info, folder):
    if os.path.exists(f"{info['title']}.mp4"):
        os.remove(f"{info['title']}.mp4")
    try:
        options = {
            'format': '136/137/mp4/bestvideo,140/m4a/bestaudio',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'keepvideo': True,
            'keepaudio': True,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([info['webpage_url']])
        return False
    except Exception as e:
        print(e)
        options = {
            'format': '136/137/mp4/bestvideo,140/m4a/bestaudio',
            'outtmpl': 'video [%(id)s].%(ext)s',
            'keepvideo': True,
            'keepaudio': True,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([info['webpage_url']])

    return True


def pitch_shift(label, info, step, rename):
    label.config(text=f"Shifting pitch of the audio by {step} steps", fg="blue")
    if rename:
        audio = f"video [{info['id']}].m4a"
    else:
        audio = f"{info['title']}[{info['id']}].m4a"
    sound = pydub.AudioSegment.from_file(audio)
    sound.export('out.wav', format='wav')
    y, sr = sf.read('out.wav')
    y_shift = pyrubberband.pitch_shift(y, sr=sr, n_steps=step)
    sf.write('outshifted.wav', y_shift, sr, format="wav")

    if rename:
        os.remove(f"video [{info['id']}].m4a")
    else:
        os.remove(f"{info['title']}[{info['id']}].m4a")
    os.remove('out.wav')


def scale_changed_video(label, info, folder, scale, rename):
    label.config(text="Merging video and pitch shifted audio", fg="blue")
    if rename:
        video = VideoFileClip(f"video [{info['id']}].mp4")
    else:
        video = VideoFileClip(f"{info['title']}[{info['id']}].mp4")
    audio = AudioFileClip('outshifted.wav')

    videoclip = video.set_audio(audio)

    if rename:
        videoclip.write_videofile(folder + info['title'][:20] + f'_scale_changed_{int(scale)}.mp4')
        os.remove(f"video [{info['id']}].mp4")
    else:
        videoclip.write_videofile(folder + info['title'] + f'_scale_changed_{int(scale)}.mp4')
        os.remove(f"{info['title']}[{info['id']}].mp4")
    os.remove('outshifted.wav')


def main(label, button, url, scale=0, output_folder='~'):
    label.config(text="Downloading..... Please wait", fg="brown")
    button.config(state="disabled")
    info = None
    try:
        info = yt_dlp.YoutubeDL().extract_info(
            url=url, download=False
        )
    except Exception as e:
        label.config(text=f"Please enter valid url", fg="red")
        print(e)

    if info:
        try:
            rename = get_original_video(label, info, output_folder)
            if scale:
                pass
                pitch_shift(label, info, int(scale), rename)
                scale_changed_video(label, info, output_folder, scale, rename)
            label.config(text=f"Download Complete!!! Videos stored to {output_folder}", fg="green")
        except Exception as e:
            print(e)
            label.config(text="An error occurred! Please close the programme and retry", fg="crimson")

    button.config(state="normal")
