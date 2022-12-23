#!/home/itachi/miniconda3/bin/python3.9
import numpy as np
import wave
from numpy.core.getlimits import MachArLike
from numpy.core.numeric import isclose
from numpy.lib.shape_base import _make_along_axis_idx
import simpleaudio as sa
import scipy.io.wavfile as wf
import sys 
import pyaudio as pa
from scipy.io.wavfile import write
from simpleaudio.shiny import play_buffer

wave_read = wave.open("C3.wav", 'rb')
audio_data = wave_read.readframes(wave_read.getnframes())
num_channels = wave_read.getnchannels()
bytes_per_sample = wave_read.getsampwidth()
sample_rate = wave_read.getframerate()

wave_obj = sa.WaveObject(audio_data, num_channels, bytes_per_sample, sample_rate)
play_obj = wave_obj.play()
play_obj.wait_done()

print(num_channels, bytes_per_sample,sample_rate)



wave_file = wave.open('C3.wav', 'rb')
samplerate, data = wf.read('C3.wav')
print(data)
bytes_per_sample = wave_file.getsampwidth()
print(bytes_per_sample)
play = sa.play_buffer(data,2,3,samplerate)
play = sa.play_buffer(data,num_channels,bytes_per_sample,samplerate)
# play.wait_done()