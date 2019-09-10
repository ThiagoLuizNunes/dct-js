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

def createAudio(name, rate, frames):
    wavfile.write('bin/'+ name + '.waw', rate, frames)
