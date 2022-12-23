#!/usr/bin/python
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

# track = Track(signature=(4,4))
# no = [note.Note('A3'),note.Note('B3'),note.Note('C3')]
# track.add(no[0])
# track.add(no[1])
# track.add(no[2])
# track.add(no)
# print(track)


# with open('chords.midi', 'wb') as f:
#     midi.dump(track, f)


class midi_Creator:
    track = Track(signature=(4,4))
    x = 0 
    midi_file = Track(signature=(4,4))
    
    def note_Mapper(self,tone):
        tone = note.Note(str(tone)+'3')
        print(str(tone)+'3')
        return tone 


    def conv_Midi_Obj(self,progression):
        prog = []
        for i in progression:
            p = list(map(self.note_Mapper,i))
            prog.append(p)
        return prog

    def creator(self,progression,arp,name):
        progression= self.conv_Midi_Obj(progression)
        print(progression)
        arp = self.conv_Midi_Obj(arp)
        print(arp)
        for i in range(0,len(progression)):
            for x in arp[i]:
                self.track.add(x)
            self.track.add(progression[i])
        self.write_midi(name)
        return self.track

    def write_midi(self,name):
        with open("{}".format(name),"wb") as f:
            midi.dump(self.track,f)
        sudoPassword = 'iwillchangetheworld'
        command = 'mv {} /var/www/html/midi_files/'.format(name)
        p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
        return (name)


# progression = [['C', 'E', 'G'], ['B', 'D', 'F#'], ['A', 'C', 'E'], ['G', 'B', 'D']]
# mc = midi_Creator()
# file = mc.creator(progression,progression)
# print(file)
# with open('ehh.midi', 'wb') as f:
#     midi.dump(file, f) 