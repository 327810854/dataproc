import soundfile as sf
import librosa
import numpy as np
import scipy.signal

def save_audio(path, y, sr):
    sf.write(path, y, sr)

def load_audio(path, sr=16000):
    y, sr = librosa.load(path, sr=sr)
    return y, sr

