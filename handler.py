#!/home/itachi/miniconda3/bin/python3.9
# from lib2to3.pytree import convert
# from os import TMP_MAX
# from queue import PriorityQueue
# import re
# from statistics import median_low
# from turtle import shape
# from typing import Final, final
# from jinja2 import ModuleLoader
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
#2646000,2 np.shape of 1m of silence
#44100 ,2 np.shape of 1s of silence
class Chord_Generator:
    global melody
    melody = np.zeros(dtype= np.int16,shape=(2,2))
    arp = np.zeros(dtype= np.int16,shape=(2,2))
    notes = []
    arp2 = np.zeros(dtype= np.int16,shape=(2,2))
    chord = np.zeros(dtype= np.int16,shape=(2,2))
    
    #                                                                                      add_padding
    
    def add_padding(self,C):
        name = "{0}3.wav".format(C)
        return name
        
    #                                                                                      __chord_creator
        
    def __chord_creator(self,notes_list):#private function 
        notes_list = map(self.add_padding,notes_list)
        self.notes_list = list(notes_list)
        self.notes = []
        for i in self.notes_list:
            samplerate , data = wf.read(i)
            self.chord = np.zeros(dtype= np.int16,shape=(data.shape))
            self.melody = np.zeros(dtype= np.int16,shape=(data.shape))
            self.notes.append(data)
        for i in self.notes:
            self.chord = np.add(self.chord,i)
            
    #                                                                                      arp_creator
    
    def __arp_creator(self,style):
        if style == 1:  #1 = up arp
            a1 = []
            a2 = []
            print("Flag")
            for i in self.notes:
                a1 = np.append(a1,i)
            play = sa.play_buffer(a1,2,2,44100)
            play.wait_done()
            for i in reversed(self.notes):
                a2 = np.append(a2,i)
            self.arp = np.append(a1,a2)
            self.melody_designer(self.chord,self.arp)
            
        elif style == 2: #2 = down arp
            for i in reversed(self.notes):
                self.arp = np.append(self.arp,i)
            self.melody_designer(self.chord,self.arp)
        
        elif style == 3: #3 = up/down arp
            for i in self.notes:
                   self.arp = np.append(self.arp,i)
            self.melody = np.append(self.arp,self.chord)
            for i in reversed(self.notes):
                self.arp2 = np.append(self.arp2,i)
            self.melody_designer(self.chord,self.arp,self.arp2,False)
        
        elif style == 4: #4 = down/up arp
            for i in reversed(self.notes):
                self.arp2 = np.append(self.arp2,i)
            for i in self.notes:
                self.arp = np.append(self.arp,i)
            self.melody_designer(self.chord,self.arp2,self.arp,False)
            
    #                                                                                      melody_designer
                
    def melody_designer(self,chord,arp1,arp2 = None,flag = True):
        if flag == True:
            
            self.melody = np.append(arp1,chord)
        else:
            self.melody = np.append(arp1,chord)
            self.melody = np.append(self.melody,arp2)
            self.melody = np.append(self.melody,chord)
            # self.play_melody()    
    
    def play_melody(self):
        play = sa.play_buffer(self.melody,2,2,44100)
        play.wait_done()
    
    #                                                                                      chord_creator
    
    def chord_creator(self,note_list):
        progression = []
        shape = np.shape(note_list[0][0])
        for i in note_list:
            sample_chord = np.zeros(dtype= np.int16,shape=(shape))
            for x in i:
                sample_chord = np.add(sample_chord,x)
            progression.append(sample_chord)
        return progression
    
    #                                                                                      binary_convertor
            
    def binary_convertor(self,note):
        samplerate , data = wf.read(note)
        # print(samplerate)
        return data
        
    #                                                                                      arp_creator
    
    def arp_creator(self,notes,style):
        style = int(style)
        arp = []
        rarp = []
        if style == 1:
            for i in notes:
                arp.append(i)
            for i in reversed(notes):
                rarp.append(i)
        if style == 2:
            for i in reversed(notes):
                arp.append(i)
        return arp
            
            
        
        
    #                                                                                      melody_creator  
    def melody_creator(self,pro,style):
        notes = []
        for i in pro:
            temp = map(self.binary_convertor,i)
            temp = list(temp)
            notes.append(temp)
        chords = self.chord_creator(notes)
        print(notes)
        
        # arp = self.arp_creator(notes) 
        melody = []
        for i in range (0,len(chords)):
            arp = self.arp_creator(notes[i],style)
            for x in arp:
                melody.append(x)
            melody.append(chords[i])
        final_melody = np.zeros(np.shape(melody[0]))
        for i in melody:
            # play = sa.play_buffer(i,2,2,44100*2)
            # play.wait_done()
            final_melody = np.append(final_melody,i)
        final_melody = final_melody = final_melody.astype('int16')

        # with wave.open("test1.wav","w") as f:
        #     f.setnchannels(2)
        #     f.setsampwidth(2)
        #     f.setframerate(75000)
        #     f.writeframes(final_melody)
            
        # write("test1.wav",44100,final_melody.astype('float64'))
        return melody
        
    #                                                                                      arp_notes
    
    def arp_notes(self,pro):
        a_notes = []
        print(len(pro))
        for i in pro:
            for x in i:
                a_notes.append(x)
        return a_notes
        
    #                                                                                      create_melody
    
    def create_melody(self,progression,style,login_id):
        progression = list(progression)
        tonic = progression[0][0]
        # pro = []
        # for i in progression:
        #     for x in i:
        #         pro.append(list(map(self.add_padding,x)))
        # chords = self.chord_creator(pro)
        # arp = self.arp_creator(tonic)
        
            # melody = self.melody_creator(pro,style)
        arp_notes = self.arp_notes(progression)
        arp_notes = self.convertor(arp_notes)
        chord_notes = arp_notes        
        chords = self.chord_manufacturer(chord_notes)
        arp_notes = self.arp_manufacturer(arp_notes,chords,style)
    #                                                                                      convertor
        
    def convertor(self,notes):
        result = []
        final = []
        for i in notes :
            temp = map(self.add_padding,i)
            temp = list(temp)
            result.append(temp)
        for i in result:
            temp = map(self.binary_convertor,i)
            temp = list(temp)
            final.append(temp)
        return final
    
    #                                                                                      chord_manufacturer
    
    def chord_manufacturer(self,chord_notes):
        chord = []
        shape = np.shape(chord_notes[0][0])
        for i in chord_notes:
            temp = np.zeros(dtype= np.int16,shape=(shape))
            for x in i:
                temp = np.add(temp,x)
            chord.append(temp)
        return chord
    
    #                                                                                      arp_mangggggggfffmufacturer
    
    def arp_manufacturer(self,notes,chords,style):
        style = str(style)
        if style == "FINE":
            self.fine(notes,chords)       
    
    #                                                                                      FINE

    def fine(self,notes,chords):
        global melody
        for i in range(0,len(chords)-1):
            j = i + 1
            print(i,j)
            for x in notes[i]:
                melody = np.append(melody,x)
            melody = np.append(melody,chords[i])
            for x in reversed(notes[j]):
                melody = np.append(melody,x)
        shape = np.shape(melody)
        print(shape)
        samplerate , data = wf.read('beat4.wav')
        shape = np.shape(data)
        print(shape)
        melody = np.add(melody,data)
        with wave.open("/var/www/html/wav_files/hello.wav","w") as f:
            f.setnchannels(2)
            f.setsampwidth(2)
            f.setframerate(80000)
            f.writeframes(melody)
        # data = np.reshape()
        print(notes[0][1].shape)
        melody = np.add(melody,data)
        play = sa.play_buffer(melody,2,2,44100*2)
        play.wait_done()
        
            
        
        
        # for i in melody:
        #     play = sa.play_buffer(i,2,2,44100)
        #     play.wait_done()   
                
    # def create_melody(self,notes):
    #     self.__chord_creator(notes)
    #     arp_type = input("Enter the arp type")
    #     arp_type = int(arp_type)
    #     self.__arp_creator(arp_type)
    #     return self.melody
    
# c = Chord_Generator();
# notes = ['C','E','G']
# song =  c.create_melody(notes)
# play = sa.play_buffer(song,2,2,44100)
# play.wait_done()
