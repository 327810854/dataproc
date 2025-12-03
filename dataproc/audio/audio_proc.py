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

def noise_reduction_simple(y, sr, cutoff=7000):
    nyq = 0.5 * sr
    norm_cutoff = cutoff / nyq
    b, a = scipy.signal.butter(6, norm_cutoff, btype='low')
    y_filt = scipy.signal.filtfilt(b, a, y)
    return y_filt

def preprocess_basic(path,
                     sr=16000,
                     top_db=20,
                     pre_emphasis_coeff=0.97,
                     noise_cutoff=7000):
    y, sr = load_audio(path, sr=sr)

    y = trim_silence(y, top_db=top_db)

    y = pre_emphasis(y, coeff=pre_emphasis_coeff)

    y = noise_reduction_simple(y, sr, cutoff=noise_cutoff)

    y = normalize_audio(y)

    return y, sr