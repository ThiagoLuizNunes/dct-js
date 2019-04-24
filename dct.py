from pydub import AudioSegment
from scipy.io import wavfile
from scipy import fftpack
from scipy.fftpack import dct
from scipy.fftpack import idct
import array as arr
import wave, struct

waveFile = wave.open('audio.wav', 'r')
rate = waveFile.getframerate()
length = waveFile.getnframes()
arrayAudioFrames = arr.array('i')
arrayAudioFramesRobot = arr.array('i')

for i in range(0,length):
  waveData = waveFile.readframes(1)
  data = struct.unpack('<h', waveData)
  arrayAudioFrames.append(int(data[0]))
  arrayAudioFramesRobot.append(abs(int(data[0])))

newArrayDCT = dct(arrayAudioFrames, norm = 'ortho')
newArrayDCTChunked = dct(arrayAudioFrames, norm = 'ortho')
newArrayDCTRobot = dct(arrayAudioFramesRobot, norm = 'ortho')

maxCosValue = 100
countCos = 0
for i in range(0, len(newArrayDCTChunked)):
  if abs(newArrayDCTChunked[i]) < maxCosValue:
    countCos += 1
    newArrayDCTChunked[i] = 0

print('Total cosine: ', len(newArrayDCTChunked))
print('Deleted cosine: ', countCos)

newArrayIDCT = idct(newArrayDCT, norm = 'ortho')
newArrayIDCT = newArrayIDCT.astype('int16')

newArrayIDCTChunked = idct(newArrayDCTChunked, norm = 'ortho')
newArrayIDCTChunked = newArrayIDCTChunked.astype('int16')

newArrayIDCTRobot = idct(newArrayDCTRobot, norm = 'ortho')
newArrayIDCTRobot = newArrayIDCTRobot.astype('int16')

wavfile.write('audio-idct.wav', rate , newArrayIDCT)
wavfile.write('audio-idct-chunked.wav', rate , newArrayIDCTChunked)
wavfile.write('audio-idct-robot.wav', rate , newArrayIDCTRobot)
