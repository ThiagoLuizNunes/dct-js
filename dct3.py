import sys
import struct
import numpy as np
from math import pi, sin, cos, radians, sqrt
import array as arr
from . import helper as hp

def alpha(k, N):
    return sqrt(1.0/N) if k == 0 else sqrt(2.0/N)
def dct_1d(audio, numberCoefficients=0):

    nc = numberCoefficients
    n = len(audio)
    newAudio = np.zeros(n).astype(float)

    for k in range(n):
        sum = 0
        for i in range(n):
            sum += audio[i] * cos(2 * pi * k / (2.0 * n)
                                  * i + (k * pi) / (2.0 * n))
        ck = sqrt(0.5) if k == 0 else 1
        newAudio[k] = sqrt(2.0 / n) * ck * sum

    # salvando os N maiores numeros e zerandos todos os outros
    if nc > 0:
        newAudio.sort()
        for i in range(nc, n):
            newAudio[i] = 0

    return newAudio  # retorno de um VETOR


def idct_1d(audio):

    n = len(audio)
    newAudio = np.zeros(n).astype(float)

    for i in range(n):
        sum = 0
        for k in range(n):
            # operador tenario para verificar o valor do CK
            ck = sqrt(0.5) if k == 0 else 1
            sum += ck * audio[k] * cos(2 * pi * k /
                                       (2.0 * n) * i + (k * pi) / (2.0 * n))

        newAudio[i] = sqrt(2.0 / n) * sum

    return newAudio
