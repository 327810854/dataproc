import soundfile as sf
import librosa
import numpy as np
import scipy.signal

def save_audio(path, y, sr):
    sf.write(path, y, sr)

def load_audio(path, sr=16000):
    y, sr = librosa.load(path, sr=sr)
    return y, sr

def normalize_audio(y):
    return librosa.util.normalize(y)

def trim_silence(y, top_db=20):
    trimmed, _ = librosa.effects.trim(y, top_db=top_db)
    return trimmed

def pre_emphasis(y, coeff=0.97):
    return np.append(y[0], y[1:] - coeff * y[:-1])