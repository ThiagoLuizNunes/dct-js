import sys
import numpy as np
from modules import helper as hp
from math import sqrt, cos, pi

def ck(k):
    return sqrt(0.5) if k == 0 else 1


def freq(n, k):
    return k / (2.0 * n)


def theta(n, k):
    return (k * pi) / (2.0 * n)


def applyDCT(signals):
    n = len(signals)
    dcLevel = np.zeros_like(signals).astype(float)
    new_signals = np.zeros_like(signals).astype(float)

    # Through cosines
    for k in range(n):
        _sum = 0
        # Through all signals
        for i in range(n):
            _sum += signals[i] * cos(2 * pi * freq(n, k) * i + theta(n, k))
            if i == 0:
              dcLevel[i] = _sum

        new_signals[k] = sqrt(2.0 / n) * ck(k) * _sum

    return new_signals


def applyIDCT(signals):
    n = len(signals)
    new_signals = np.zeros_like(signals).astype(float)

    # Through all signals
    for i in range(n):
        _sum = 0
        # Through cosines
        for k in range(n):
            _sum += ck(k) * signals[k] * cos(2 * pi * freq(n, k) * i + theta(n, k))

        new_signals[i] = sqrt(2.0 / n) * _sum

    return new_signals


def applyIDCT2D(signals):
    height = signals.shape[0]
    width = signals.shape[1]
    new_signals_1 = np.zeros_like(signals).astype(float)
    new_signals_2 = np.zeros_like(signals).astype(float)

    # Apply IDCT on all rows
    for h in range(height):
        new_signals_1[h, :] = applyIDCT(signals[h, :])
    # Apply IDCT on all columns of the previous result
    for w in range(width):
        new_signals_2[:, w] = applyIDCT(new_signals_1[:, w])

    return new_signals_2


def applyDCT2D(signals, coef=0):
    height = signals.shape[0]
    width = signals.shape[1]
    new_signals_1 = np.zeros_like(signals).astype(float)
    new_signals_2 = np.zeros_like(signals).astype(float)

    # Apply DCT on all rows
    for h in range(height):
        new_signals_1[h, :] = applyDCT(signals[h, :])
    # Apply DCT on all columns of the previous result
    for w in range(width):
        new_signals_2[:, w] = applyDCT(new_signals_1[:, w])

    return new_signals_2

if __name__ == '__main__':
    path = sys.argv[1]
    amount = sys.argv[2]

    if ('.bmp' in path) or ('.jpg' in path):
        frames = hp.openImage(path)
        cosines = applyDCT2D(frames, amount)
        mostCosines2D = hp.mostImportantsCoeff2D(cosines, amount)
        hp.createImage('dct', mostCosines2D)
        signal = applyIDCT2D(mostCosines2D)
        hp.createImage('coeff', signal)
    if '.wav' in path:
        rate, frames = hp.openAudio(path)
        cosines = applyDCT(frames)
        mostCosines = hp.mostImportantsCoeff(cosines, amount)
        hp.showGraph('Most importants cosines', mostCosines)
        signal = applyIDCT(mostCosines)
        hp.createAudio('coeff', rate, signal)

    # ekCosines = [10, 5, 8.5, 2, 1, 1.5, 0, 0.1]
    # signal = applyIDCT(ekCosines)
    # cosines = applyDCT(signal)
    # print('Signal:', signal)
    # print('Cosines:', cosines)
    # hp.showGraph('Signal', cosines)


