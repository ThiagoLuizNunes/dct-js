import sys
import wave
import struct
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos, radians, sqrt
from scipy.io import wavfile
from PIL import Image
import array as arr
from modules import helper as hp


def ck(k):
    return sqrt(0.5) if k == 0 else 1


def freq(n, k):
    return k / (2.0 * n)


def theta(n, k):
    return (k * pi) / (2.0 * n)


def dct(signals):
    n = len(signals)
    new_signals = np.zeros_like(signals).astype(float)

    for k in range(n):
        _sum = 0
        for i in range(n):
            _sum += signals[i] * cos(2 * pi * freq(n, k) * i + theta(n, k))

        new_signals[k] = sqrt(2.0 / n) * ck(k) * _sum

    return new_signals


def idct(signals):
    n = len(signals)
    new_signals = np.zeros_like(signals).astype(float)

    for i in range(n):
        _sum = 0
        for k in range(n):
            _sum += ck(k) * signals[k] * cos(2 * pi * freq(n, k) * i + theta(n, k))

        new_signals[i] = sqrt(2.0 / n) * _sum

    return new_signals

if __name__ == '__main__':
    path = sys.argv[1]
    rate, frames = hp.openAudio(path)
    ekCosines = [10, 5, 8.5, 2, 1, 1.5, 0, 0.1]

    signal = idct(ekCosines)
    cosines = dct(signal)
    print(signal)
    print(cosines)
    hp.showGraph('Signal', cosines)
