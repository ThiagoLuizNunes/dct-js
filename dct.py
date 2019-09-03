import sys
import wave
import struct
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin, cos, radians, sqrt
from scipy.io import wavfile
from PIL import Image
import array as arr
# DCT Audio


def openAudio(rate):
    waveFile = wave.open('audio.wav', 'r')
    # rate = waveFile.getframerate()
    length = waveFile.getnframes()
    arrayAudioFrames = arr.array('i')

    for i in range(0, length):
        waveData = waveFile.readframes(1)
        data = struct.unpack('<h', waveData)
        if abs(int(data[0])) > rate:
            arrayAudioFrames.append(int(data[0]))
    return arrayAudioFrames


def showDCTGraph(dcts):
    arr = np.arange(len(dcts))
    plt.plot(arr, dcts)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('DCT graph')
    plt.show()


def applayDCTinAudio(frames):
    N = len(frames)
    print(N)
    cosines = np.zeros(N)
    # N = 8
    # ex = [10, 5, 8.5, 2, 1, 1.5, 0, 0.1]
    for k in range(0, N):
        ck = sqrt(0.5) if k == 0 else 1
        Ak = sqrt(2/N)
        Xk = frames[k]
        samples = np.zeros(N)
        # Xk = ex[k]

        for n in range(0, N):
            samples[n] = Ak * ck * Xk * \
                cos(radians(((2*pi*k*n)/2*N) + ((k*pi)/2*N)))
            cosines[n] = cosines[n] + samples[n]

    arr = np.arange(N)
    plt.plot(arr, cosines)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('DCT')
    plt.show()


if __name__ == '__main__':
    rate = sys.argv[1]
    print(rate)
    frames = openAudio(int(rate))
    applayDCTinAudio(frames)
    # showDCTGraph(frames)
    # applayDCTinAudio(frames)
    # newArrayDCT = dct(arrayAudioFrames, norm = 'ortho')

    # newArrayIDCT = idct(newArrayDCT, norm = 'ortho')
    # newArrayIDCT = newArrayIDCT.astype('int16')

    # wavfile.write('audio-idct.wav', rate , newArrayIDCT)
    # wavfile.write('audio-idct-chunked.wav', rate , newArrayIDCTChunked)
    # wavfile.write('audio-idct-robot.wav', rate , newArrayIDCTRobot)

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
