#!/usr/bin/python
import datetime
import numpy as np
from numpy.core.getlimits import MachArLike
from numpy.core.numeric import isclose
from numpy.lib.shape_base import _make_along_axis_idx
import simpleaudio as sa
import scipy.io.wavfile as wf
# import sys 
import wave
from scipy.io.wavfile import write
from simpleaudio.shiny import play_buffer
progression = [['C', 'E', 'G'], ['B', 'D', 'F#'], ['A', 'C', 'E'], ['G', 'B', 'D']]
samplerate , data = wf.read('notes/A3.wav')

class chord_Generator:
    def __init__(self):
        pass
        # print("Class created")

    def create_Arp(self,progression,style):
        arp = []
        if style == 1:
            for x in progression:
                sarp = []
                for y in x:
                    sarp.append(y)
                print(sarp)
                arp.append(sarp)
            return(arp)
        elif style == 2:
            for x in progression:
                sarp = []
                for y in reversed(range(len(x))):
                    sarp.append(x[y])
                print(sarp)
                arp.append(sarp)
            return(arp)
        elif style == 3:
            for x in range(0,len(progression),2):
                sarp = []
                sarp_2 = []
                for i in progression[x]:
                    sarp.append(i)
                arp.append(sarp)
                for i in range(len(progression[x+1])-1,-1,-1):
                    sarp_2.append(progression[x+1][i])
                arp.append(sarp_2)
            return(arp)
        elif style == 4:
            for x in range(1,len(progression),2):
                sarp = []
                sarp_2 = []
                for i in progression[x]:
                    sarp.append(i)
                for i in range(len(progression[x-1])-1,-1,-1):
                    sarp_2.append(progression[x-1][i])
                arp.append(sarp_2)
                arp.append(sarp)
            return(arp)
    
    def add_Padding(self,C):            #adding_path
        name = "notes/{0}3.wav".format(C)
        return name

    def convert_Wav(self,note):        #converting_into_wav_format
        samplerate,data = wf.read(note)
        return data

    def create_Name(self,uid):
        name = str(datetime.date.today()) + "-" + str(uid)
        wfl = name + ".wav"
        mfl = name + ".midi"
        return wfl,mfl

    def get_Wav(self,progression,arpe):
        prog = []
        arp = []
        for i in progression:
            prog.append(list(map(self.convert_Wav,map(self.add_Padding,i))))
        for i in arpe:
            arp.append(list(map(self.convert_Wav,map(self.add_Padding,i))))
        chords = self.create_Chords(prog)
        return chords,arp

    def create_Chords(self,progression):
        chords = []
        for i in progression:
            indi_Chord = np.zeros(dtype= np.int16,shape=(data.shape))
            for j in i:
                indi_Chord = np.add(indi_Chord,j)
            chords.append(indi_Chord)
        return(chords)

    def create_Melody(self,progression,uid):
        arp = self.create_Arp(progression,4)
        chordsByte,arpByte = self.get_Wav(progression,arp)
        wfl,mfl = self.create_Name(uid)
        return arp,chordsByte,arpByte,wfl,mfl
    def rectify_progression(self,progression):
        prog = []
        for i in progression:
            for x in i:
                prog.append(x)
        return prog

# x= [1,2,3,4,5,6]

# for i in range(len(x)-1,0,-2):
# #     print(i)

c = chord_Generator()
c.create_Name('003')
# arp,chordsbyte,arpbyte =  c.create_Melody(progression)
# print(arp)
# arp = c.create_Arp(progression,4)
# chordsByte,arpByte = c.get_Wav(progression,arp)
# # chords = c.create_Chords(progression)
# print(progression,arp)