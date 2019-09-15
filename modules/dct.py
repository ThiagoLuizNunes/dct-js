import numpy as np
from math import sqrt, cos, pi

def ck(k):
    return sqrt(0.5) if k == 0 else 1


def freq(N, k):
    return k / (2.0 * N)


def theta(N, k):
    return (k * pi) / (2.0 * N)


def applyDCT(signal):
    N = len(signal)
    cosines = np.zeros_like(signal).astype(float)

    # Through cosines
    for k in range(N):
        _sum = 0
        # Through all signal
        for i in range(N):
            _sum += signal[i] * cos(2 * pi * freq(N, k) * i + theta(N, k))

        cosines[k] = sqrt(2.0 / N) * ck(k) * _sum

    return cosines


def applyIDCT(cosines):
    N = len(cosines)
    signal = np.zeros_like(cosines).astype(float)

    # Through all cosines
    for i in range(N):
        _sum = 0
        # Through cosines
        for k in range(N):
            _sum += ck(k) * cosines[k] * cos(2 * pi * freq(N, k) * i + theta(N, k))

        signal[i] = sqrt(2.0 / N) * _sum

    return signal


def applyIDCT2D(cosines):
    height = cosines.shape[0]
    width = cosines.shape[1]
    cosines_1 = np.zeros_like(cosines).astype(float)
    cosines_2 = np.zeros_like(cosines).astype(float)

    # Apply IDCT on all rows
    for h in range(height):
        cosines_1[h, :] = applyIDCT(cosines[h, :])
    # Apply IDCT on all columns of the previous result
    for w in range(width):
        cosines_2[:, w] = applyIDCT(cosines_1[:, w])

    return cosines_2


def applyDCT2D(signal):
    height = signal.shape[0]
    width = signal.shape[1]
    signal_1 = np.zeros_like(signal).astype(float)
    signal_2 = np.zeros_like(signal).astype(float)

    # Apply DCT on all rows
    for h in range(height):
        signal_1[h, :] = applyDCT(signal[h, :])
    # Apply DCT on all columns of the previous result
    for w in range(width):
        signal_2[:, w] = applyDCT(signal_1[:, w])

    return signal_2

def deslocateFreq(cosines, inc):
    N = len(cosines)
    deslocateCosines = np.zeros_like(cosines).astype(float)

    for i in range(0, N):
        if i + int(inc) < N:
          deslocateCosines[i] = cosines[i + int(inc)]
        else:
          deslocateCosines[i] = 0

    return deslocateCosines
