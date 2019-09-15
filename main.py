import sys
from modules import helper as hp
from modules import dct

if __name__ == '__main__':
    path = sys.argv[1]
    choose = sys.argv[2]
    amount = sys.argv[3]

    if choose == '1':
        frames = hp.openImage(path)
        cosines = dct.applyDCT2D(frames)
        mostCosines2D = hp.mostImportantsCoeff2D(cosines, amount)
        hp.createImage('dct', mostCosines2D)
        signal = dct.applyIDCT2D(mostCosines2D)
        hp.createImage('coeff', signal)
    if choose == '2':
        rate, frames = hp.openAudio(path)
        cosines = dct.applyDCT(frames)
        mostCosines = hp.mostImportantsCoeff(cosines, amount)
        hp.showGraph('Most importants cosines', mostCosines)
        signal = dct.applyIDCT(mostCosines)
        hp.createAudio('coeff', rate, signal)
    if choose == '3':
        rate, frames = hp.openAudio(path)
        cosines = dct.applyDCT(frames)
        deslocateCosines = dct.deslocateFreq(cosines, amount)
        hp.showGraph('Dislocated cosines', deslocateCosines)
        signal = dct.applyIDCT(deslocateCosines)
        hp.createAudio('coeff', rate, signal)
    if choose == '4':
        ekCosines = [10, 5, 8.5, 2, 1, 1.5, 0, 0.1]
        signal = dct.applyIDCT(ekCosines)
        cosines = dct.applyDCT(signal)
        print('Signal:', signal)
        print('Cosines:', cosines)
        hp.showGraph('Signal', cosines)
