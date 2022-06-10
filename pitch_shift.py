import librosa
import soundfile as sf
import os


def pitch_shift(folder, title, step):
    y, sr = librosa.load(folder + title + '.f140.m4a')

    y_shift = librosa.effects.pitch_shift(y, sr=sr, n_steps=step)
    sf.write('outshifted.wav', y_shift, sr, format="wav")

    os.remove(folder + title + '.f140.m4a')
