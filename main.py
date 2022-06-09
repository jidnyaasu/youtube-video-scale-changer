import yt_dlp
from pitch_shift import pitch_shift
from scale_changed_video import scale_changed_video


def get_raw_audio(video_info):
    options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'outtmpl': f"out.wav",
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])


def get_only_video(video_info):
    options = {
        'format': 'bestvideo[ext=mp4]/best',
        'outtmpl': f"out.mp4",
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])


def get_original_video(video_info, folder):
    options = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        'outtmpl': f"{folder}{video_info['title']}.mp4",
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])


def main(url, scale=0, output_folder='~'):
    info = yt_dlp.YoutubeDL().extract_info(
        url=url, download=False
    )
    get_original_video(info, output_folder)
    if scale:
        get_raw_audio(info)
        get_only_video(info)
        pitch_shift(int(scale))
        scale_changed_video(output_folder, info['title'], scale)

    return "Download complete!"
