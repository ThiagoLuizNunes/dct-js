from pydub import AudioSegment

song = AudioSegment.from_wav("audio.wav")

_previous = 0
_next = 1

for x in range(0, 3000):
  sample = song[_previous : _next]
  sample.export('./samples/sample' + str(_previous) +'.wav', format="wav")
  _previous += 1
  _next += 1
