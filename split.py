from pydub import AudioSegment
from scipy.io import wavfile
from scipy import fftpack
from scipy.fftpack import dct
from scipy.fftpack import idct
import array as arr
import wave, struct

# rate, audioData = wavfile.read('audio.wav')
# newDCTAudio = dct(audioData)
# print(newDCTAudio)

waveFile = wave.open('audio.wav', 'r')
rate = waveFile.getframerate()
length = waveFile.getnframes()
arrayAudioFrames = arr.array('i')

for i in range(0,length):
  waveData = waveFile.readframes(1)
  data = struct.unpack('<h', waveData)
  # arrayAudioFrames.append(int(data[0]))
  arrayAudioFrames.append(abs(int(data[0])))

newArrayDCT = dct(arrayAudioFrames, norm = 'ortho')
# for i in range(0, len(newArrayDCT)):
#   newArrayDCT[i] = abs(newArrayDCT[i])

newArrayIDCT = idct(newArrayDCT, norm = 'ortho')
newArrayIDCT = newArrayIDCT.astype('int16')
# for i in range(0, len(newArrayIDCT)):
#   newArrayIDCT[i] = abs(newArrayIDCT[i])

print(newArrayDCT)
print(newArrayIDCT)

wavfile.write('audio-dct.wav', rate , newArrayDCT)
wavfile.write('audio-idct.wav', rate , newArrayIDCT)
