#!/home/itachi/miniconda3/bin/python3.9
from multiprocessing.connection import wait
from re import M, T
from flask import *
import json
import numpy as np
import scipy.io.wavfile as wf 
import simpleaudio as sa
import wave as w


def r():
    # samplerate , data = wf.read('excuses.wav')
    ob = w.open('excuses.wav','rb')
    f = ob.getnframes()
    data = []
    for i in range(0,f):
        frames = ob.readframes(i)
        data.append(frames)
    return data,f
