import sys
import wave
import struct
import numpy as np
from math import pi, sin, cos, radians, sqrt
import array as arr
from modules import helper as hp


def applyDCTinAudio(signal):
    N = len(signal)
    cosines = np.zeros(N).astype(float)

    for k in range(0, N):
        alpha = sqrt(0.5) if k == 0 else 1
        Ak = sqrt(2/N)
        xn = signal[k]
        samples = np.zeros(N).astype(float)

        for n in range(0, N):
            samples[n] = Ak * alpha * xn * \
                cos(radians(((2*pi*k*n)/2*N) + ((k*pi)/2*N)))
            cosines[n] = cosines[n] + samples[n]

    return cosines


def applyIDCTinAudio(cosines):
    N = len(cosines)
    signal = np.zeros(N).astype(float)
    for n in range(0, N):
        Ak = sqrt(2/N)
        Xk = cosines[n]
        samples = np.zeros(N).astype(float)

        for k in range(0, N):
            alpha = sqrt(0.5) if k == 0 else 1
            samples[k] = Ak * alpha * Xk * \
                cos(radians(((2*pi*k*n)/2*N) + ((k*pi)/2*N)))
            signal[k] = signal[k] + samples[k]

    return signal




if __name__ == '__main__':
    path = sys.argv[1]
    rate, frames = hp.openAudio(path)
    # ek = [10, 5, 8.5, 2, 1, 1.5, 0, 0.1]

    signal = applyDCTinAudio(frames)
    cosines = applyIDCTinAudio(signal)
    # print(cosines)
    hp.createAudio('new-audio', rate, cosines)
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
