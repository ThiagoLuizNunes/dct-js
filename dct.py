import sys
import wave
import struct
import numpy as np
from math import pi, sin, cos, radians, sqrt
import array as arr
from modules import helper as hp


def applyIDCTinAudio(cosines):
    N = len(cosines)
    signal = np.zeros(N).astype(float)

    Ak = sqrt(2/N)
    for k in range(0, N):
        Xk = cosines[k]
        samples = np.zeros(N).astype(float)
        alpha = sqrt(0.5) if k == 0 else 1

        for n in range(0, N):
            samples[n] = Ak * alpha * Xk * \
                cos(radians(((2*pi*k*n)/2*N) + ((k*pi)/2*N)))
            signal[n] += samples[n]

    # hp.coeffStrategyOne(cosines, amount)

    return signal


def applyDCTinAudio(signal):
    N = len(signal)
    cosines = np.zeros(N).astype(float)

    Ak = sqrt(2/N)

    for n in range(0, N):
        xn = signal[n]
        samples = np.zeros(N).astype(float)

        for k in range(0, N):
            alpha = sqrt(0.5) if n == 0 else 1
            samples[k] = Ak * alpha * xn * \
                cos(radians(((2*pi*k*n)/2*N) + ((k*pi)/2*N)))
            cosines[k] += samples[k]

    return cosines


if __name__ == '__main__':
    path = sys.argv[1]
    amount = sys.argv[2]
    rate, frames = hp.openAudio(path)
    ekCosines = [10, 5, 8.5, 2, 1, 1.5, 0, 0.1]
    # ekSignal = [11.27835905, 5.00920938, 1.58139772, -0.10615071, -0.13384486, 2.87767395, 4.18172419, 4.06081887]

    signal = applyIDCTinAudio(ekCosines)
    cosines = applyDCTinAudio(signal)
    print(signal)
    hp.showGraph('Cosines', signal)
    print(cosines)
    hp.showGraph('Signal', cosines)
    # hp.createAudio('coeff', rate, cosines)
    # hp.showGraph('DCT', signal)
    # hp.showGraph('IDCT', cosines)

    # newArrayDCT = dct(arrayAudioFrames, norm = 'ortho')

    # newArrayIDCT = idct(newArrayDCT, norm = 'ortho')
    # newArrayIDCT = newArrayIDCT.astype('int16')

    # DCT Image
    # img = Image.open('lena.bmp')
    # arrayImg = np.asarray(img)

    # newImgDCT = dct(dct(arrayImg.T, norm = 'ortho').T, norm = 'ortho')
    # maxCosValueImg = 5
    # countCosImg = 0

    # for i in range(0, len(newImgDCT)):
    #   for j in range(0, len(newImgDCT[i])):
    #     if newImgDCT[i][j] < maxCosValueImg:
    #       newImgDCT[i][j] = 0
    #       countCosImg += 1

    # print('Total cosine deleted: ', countCosImg)
    # newImgIDCT = idct(idct(newImgDCT.T, norm = 'ortho').T, norm = 'ortho')
    # im = Image.fromarray(newImgIDCT)
    # im.show()
