import numpy as np
from scipy import signal


def __bandpass_filter(data: list, f1: int, f2: int) -> np.ndarray:
    b, a = signal.butter(6, [f1, f2], 'bp', fs=1000)
    filtered = signal.filtfilt(b, a, data, axis=1)
    return filtered


def __notch_filter(data: list, freq: int) -> np.ndarray:
    b, a = signal.iirnotch(freq, 30, 1000)
    filtered = signal.filtfilt(b, a, data, axis=1)
    return filtered


def filer_traces(data: list) -> np.ndarray:
    filtered = __bandpass_filter(data, 15, 60)
    filtered2 = __notch_filter(filtered, 20)
    filtered3 = __notch_filter(filtered2, 40)
    filtered4 = __notch_filter(filtered3, 50)
    return filtered4
