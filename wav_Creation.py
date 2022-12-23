import scipy.io.wavfile as wf
import numpy as np
import os
class wav_Creation:
    def __init__(self):
        pass
    def create_Wav(self,chordsbyte,arpbyte,name):
        melody = np.zeros(dtype= np.int16,shape=(arpbyte[0][0].shape))
        for i in range(0,len(chordsbyte)):
            for j in arpbyte[i]:
                melody = np.append(melody,j)
            melody = np.append(melody,chordsbyte[i])
        wf.write(name,44100,melody)
        sudoPassword = 'iwillchangetheworld'
        command = 'mv {} /var/www/html/wav_files/'.format(name)
        p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        print('wav created')
        return 'hehe'