import wave
import struct
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from PIL import Image
import array as arr


def openAudio(path):
    waveFile = wave.open(path, 'r')
    rate = waveFile.getframerate()
    length = waveFile.getnframes()
    arrayAudioFrames = arr.array('i')

    for i in range(0, length):
        waveData = waveFile.readframes(1)
        data = struct.unpack('<h', waveData)
        arrayAudioFrames.append(int(data[0]))
    return rate, arrayAudioFrames


def showGraph(label, cosines):
    arr = np.arange(len(cosines))
    plt.plot(arr, cosines)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title(label)
    plt.show()


def coeffStrategyOne(cosines, amount):
    N = len(cosines)
    coeff = np.zeros(int(amount)).astype(float)
    if int(amount) > 0:
        amountSize = int(int(amount)/2)
        cosines.sort()
        for i in range(0, amountSize):
            coeff[i] = cosines[i]
        for j in range(0, amountSize):
            coeff[amountSize + j] = cosines[N-1-j]
        showGraph('Most important coefficients', coeff)


class Cosine:
    def __init__(self, value, index):
        self.value = value
        self.index = index


def getValue(elem):
    return abs(elem.value)


def getIndex(elem):
    return abs(elem.index)


def mostImportantsCoeff(cosines, amount):
    N = len(cosines)

    cosinesList = []
    mostImportants = []
    if int(amount) > 0:
        for i in range(0, N):
            cosine = Cosine(cosines[i], i)
            cosinesList.append(cosine)
        cosinesList.sort(key=getValue)
        cosinesList.reverse()

        for x in range(0, N):
            if x > int(amount):
                cosinesList[x].value = 0
        cosinesList.sort(key=getIndex)

        for c in range(0, N):
            mostImportants.append(cosinesList[c].value)

    return mostImportants


def createAudio(name, rate, frames):
    wavfile.write('build/' + name + '.waw', rate, frames)
