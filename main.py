import yt_dlp
from pitch_shift import pitch_shift
from scale_changed_video import scale_changed_video


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


def main(url, scale=0, output_folder='~'):
    info = yt_dlp.YoutubeDL().extract_info(
        url=url, download=False
    )
    get_original_video(info, output_folder)
    if scale:
        pitch_shift(output_folder, info['title'], int(scale))
        scale_changed_video(output_folder, info['title'], scale)

    return "Download complete!"
