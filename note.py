#!/home/itachi/miniconda3/bin/python3.9
from cgi import print_directory
import threading
import midi
# from midi import Midi_Creator
import handler
import wav_Creation
import random
import numpy as np
import scipy.io.wavfile as wf
import simpleaudio as sa
import random
# from midi import *
from wav_Creation import *


Notes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

class scale_generator:
    global type_of_chord
    type_of_chord = []
    def major_scale(self,note):
        global Notes
        major_scale = []
        index = Notes.index(note)
        major_scale.append(note)
        major_scale_range = [2,2,1,2,2,2,1]
        for i in major_scale_range:
            index = index + i
            if index > len(Notes)-1:
                index = index - len(Notes)
            major_scale.append(Notes[index])
        return major_scale
        
    def major_chord(self, note):
        major_scale = self.major_scale(note)
        major_notes = []
        major_notes.append(note)
        index = major_scale.index(note)
        major_range = [2,2]
        for i in major_range:
            index = index + i
            major_notes.append(major_scale[index])
        major_notes = list(major_notes)
        return major_notes
                        
    def minor_scale(self,note):
        global Notes
        minor_scale=[]
        minor_scale.append(note)
        index = Notes.index(note)
        minor_scale_range = [2,1,2,2,1,2,2]
        for i in minor_scale_range:
            index = index + i
            if index > len(Notes)-1:
                index = index - len(Notes)
            minor_scale.append(Notes[index])
        return minor_scale
    
    def minor_chord(self,note):
        minor_notes = []
        minor_notes.append(note)
        minor_scale = self.minor_scale(note)
        index = minor_scale.index(note)
        minor_range = [2,2]
        for i in minor_range:
            index = index + i
            minor_notes.append(minor_scale[index])
        return minor_notes
    

    def harmonic_minor_scale(self,note):
        global Notes
        harmonic_minor_scale=[]
        harmonic_minor_scale.append(note)
        index = Notes.index(note)
        harmonic_minor_scale_range = [2,1,2,2,1,3,1] #harmonic_minor step counts
        for i in harmonic_minor_scale_range:
            index = index + i
            if index > len(Notes)-1:
                index = index - len(Notes)
            harmonic_minor_scale.append(Notes[index])
        return harmonic_minor_scale
    
    def harmonic_major_scale(self,note):
        global Notes
        harmonic_major_scale=[]
        harmonic_major_scale.append(note)
        index = Notes.index(note)
        harmonic_major_scale_range = [2,2,1,2,1,3,1] #harmonic_major step counts
        for i in harmonic_major_scale_range:
            index = index + i
            if index > len(Notes)-1:
                index = index - len(Notes)
            harmonic_major_scale.append(Notes[index])
        return harmonic_major_scale
        
    def first_tonic(self,scale):
        global type_of_chord
        tonic_notes = []
        tonic_notes.append(scale[0])
        tonic_notes.append(scale[2])
        tonic_chords = []
        x = random.randint(0,1)
        if x == 0:
            type_of_chord.append('{0}M'.format(tonic_notes[0]))
            chord = self.major_chord(tonic_notes[0])
            tonic_chords.append(chord)
        if x == 1:
            type_of_chord.append('{0}m'.format(tonic_notes[0]))
            chord = self.minor_chord(tonic_notes[0])
            tonic_chords.append(chord)
        return tonic_chords    
        
        
    def tonic(self,scale):
        global type_of_chord
        tonic_notes = []
        tonic_notes.append(scale[0])
        tonic_notes.append(scale[2])
        tonic_chords = []
        x = random.randint(0,1)
        if x == 0:
            type_of_chord.append('{0}M'.format(tonic_notes[0]))
            chord = self.major_chord(tonic_notes[0])
            tonic_chords.append(chord)
        if x == 1:
            type_of_chord.append('{0}m'.format(tonic_notes[1]))
            chord = self.minor_chord(tonic_notes[1])
            tonic_chords.append(chord)
        return tonic_chords
    
    def subdominant(self,scale):
        global type_of_chord
        subdominant_notes = []
        subdominant_notes.append(scale[1])
        subdominant_notes.append(scale[3])
        subdominant_notes.append(scale[5])
        subdominant_chords = []
        x = random.randint(0,2)
        x = random.randint(0,2)
        if x == 0:
            type_of_chord.append('{0}m'.format(subdominant_notes[0]))
            chord = self.minor_chord(subdominant_notes[0])
            subdominant_chords.append(chord)
        elif x == 1:
            type_of_chord.append('{0}M'.format(subdominant_notes[1]))
            chord = self.major_chord(subdominant_notes[1])
            subdominant_chords.append(chord)
        elif x == 2:
            type_of_chord.append('{0}m'.format(subdominant_notes[2]))
            chord = self.minor_chord(subdominant_notes[2])
            subdominant_chords.append(chord)
        return subdominant_chords
        
    def dominant(self,scale):
        dominant_notes = []
        dominant_notes.append(scale[4])
        dominant_notes.append(scale[6])
        dominant_chords = []
        x = random.randint(0,1)
        if x == 0:
            type_of_chord.append('{0}M'.format(dominant_notes[0]))
            chord = self.major_chord(dominant_notes[0])
            dominant_chords.append(chord)
        if x == 1:
            type_of_chord.append('{0}m'.format(dominant_notes[1]))
            chord = self.minor_chord(dominant_notes[1])
            dominant_chords.append(chord)
        return dominant_chords    
        

        
    def diminished_chord(self,note):
        global Notes
        diminished_notes = []
        diminished_notes.append(note)
        major_chord = self.major_chord(note)
        index = []
        for i in major_chord:
            index.append(Notes.index(i))
        for i in [1,2]:
            diminished_notes.append(Notes[index[i]-1])
        return(diminished_notes)
    
    def player(self,note,scale):
        scale = int(scale)
        if scale == 1:
            scale = self.major_scale(note)
        elif scale == 2:
            scale = self.minor_scale(note)
        elif scale == 3:
            scale = self.harmonic_major_scale(note)
        elif scale == 4:
            scale = self.harmonic_minor_scale(note)
        else:
            print("Invalid option")
            quit()
        progression = self.melody(scale)
        return progression
        
    def melody(self,scale):
        func = ['self.tonic(scale)','self.subdominant(scale)','self.dominant(scale)']
        progression = []
        progression.append(self.first_tonic(scale))
        temp = 0
        for i in range(0,3):
            x = random.randint(0,2)
            if x == temp:
                x = random.randint(0,2)
                # if x == temp:
                #     x = random.randint(0,2)
            progression.append(eval(func[x]))
            
        return progression

    def create_scale(self,note):
        major_notes = self.__major_chord(note)
        return major_notes
    
    def create_progression(self,note,scale,arp,uid=777):
        global type_of_chord
        type_of_chord = []
        progression = self.player(note,scale)
        progression = self.rectify_progression(progression)
        print(progression)
        c = handler.chord_Generator()
        arp,chordsbyte,arpbyte,wfn,mfn = c.create_Melody(progression,uid)
        chord = type_of_chord
        c = wav_Creation()
        file_name = c.create_Wav(chordsbyte,arpbyte,wfn)
        m = midi.midi_Creator()
        midi_fn = m.creator(progression,arp,mfn)
        return(progression,chord,wfn,mfn)
        
        
    def rectify_progression(self,progression):
        prog = []
        for i in progression:
            for x in i:
                prog.append(x)
        return prog

# c = scale_generator()
# c.create_progression("C",1,1)

#WAV CREATION PROCESS CALLED 
# c = wav_creation()
# file_name = c.create_wav(progression,arp,111)

# MIDI CREATION PROCESS CALLED
# m = Midi_Creator()
# m.creator(progression,arp)