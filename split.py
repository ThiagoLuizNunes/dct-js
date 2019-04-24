from pydub import AudioSegment
from scipy.io import wavfile
from scipy import fftpack
from scipy.fftpack import dct
from scipy.fftpack import idct
import array as arr
import wave, struct

waveFile = wave.open('audio.wav', 'r')
length = waveFile.getnframes()
arrayAudioFrames = arr.array('i')

for i in range(0,length):
  waveData = waveFile.readframes(1)
  data = struct.unpack("<h", waveData)
  arrayAudioFrames.append(int(data[0]))

newArrayDCT = dct(arrayAudioFrames)
newArrayIDCT = idct(newArrayDCT)

wavfile.write('newaudio.wav', 50000 , newArrayIDCT)

# for x in range(0, 3000):
#   sample = song[_previous : _next]
#   sample.export('./samples/sample' + str(_previous) +'.wav', format="wav")
#   _previous += 1
#   _next += 1
