def pitch_shift(step):
    import librosa
    import soundfile as sf
    import os

    y, sr = librosa.load('out.wav', sr=44100)

    y_shift = librosa.effects.pitch_shift(y, sr=sr, n_steps=step)
    sf.write('outshift.wav', y_shift, sr, format="wav")

    os.remove('out.wav')
