#!/home/itachi/miniconda3/bin/python3.9
from re import S
from signal import Signals
import os
from turtle import pen
from melodia.core import Track
from melodia.core import note
from melodia.music import chord
from melodia.io import midi
import random
from datetime import datetime
from player import r

class Midi_Creator:
    x = 0
    midi_file = Track(signature=(4,4))

    def add_padding(self,C):
        name = "{0}3.wav".format(C)
        return name

    def get_arp(self,prog,style): 
        style = int(style)
        
        if style == 1:
            arp = self.fine(prog)
            return arp
        if style == 2:
            arp = self.dream(prog)
            return arp
        if style == 3:
            arp = self.mono(prog)
            return arp
        if style == 4:
            arp = self.random(prog)
            return arp

    def create_midi(self,prog,arp,name):
        
        notes = []
        self.midi_file = Track(signature=(4,4))
        for x in prog:
            notes.append(list(map(self.add_padding,x)))
        arp = self.get_arp(notes,arp)
        for i in range(0,len(notes)):
            self.chord(notes[i])
            self.arp(arp[i])
        name = self.write_midi(name)
        return name
        
    def write_midi(self,name):
        with open("{}.midi".format(name),"wb") as f:
            midi.dump(self.midi_file,f,bpm=600)
        name = name + ".midi"
        sudoPassword = 'iwillchangetheworld'
        command = 'mv {} /var/www/html/midi_files/'.format(name)
        p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        return (name)
        
    def chord(self,prog): 
        for i in prog:
            self.midi_file.add(note.Note(i),(self.x,1))
                
    def arp(self,prog):
        self.x = self.x + 1 
        print(prog)
        print(prog[0])
        for i in range(0,3):
            self.midi_file.add(note.Note(prog[i]),(self.x,1))
            self.x = self.x + 1
            
    def fine(self,prog):
        arp = []
        for x in prog:
            mini_arp=[]
            for y in range(0,3):
                mini_arp.append(x[y])
            arp.append(mini_arp)
        return(arp)
        
    def mono(self, prog):
        arp = []
        f = 0
        for x in prog:
            if f > 2:
                f = 2
            mini_arp=[]
            for y in range(0,3):
                mini_arp.append(x[f])
            arp.append(mini_arp)
            f = f + 1
        return(arp)

    def dream(self, prog):
        arp = []
        for x in range(0,4):
            mini_arp = []
            for y in range(0,4):
                if x > 2:
                    x = 1
                mini_arp.append(prog[y][x])
            arp.append(mini_arp)
        return(arp)


    # def random(self, prog):
    #     arp = []
    #     print(prog)
    #     for x in range(0,3):
    #         mini_arp = []
    #         for y in range(0,4):
    #             i = random.randint(0,2)
    #             print(prog[i][i])
    #             mini_arp.append(prog[i][i])
    #         arp.append(mini_arp)
    #     return(arp)
        