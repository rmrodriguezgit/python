#https://pypi.org/project/playsound/

import numpy as np
import simpleaudio as sa

def reproduce_frecuencia(freq,seconds):
    fs = 44100
    #seconds = 3

    t = np.linspace(.0, seconds, seconds * fs, False)
    for frec in freq:
        note = np.sin(float(frec) * t * 2 * np.pi)
        audio = note * (2**15 - 1) / np.max(np.abs(note))
        audio = audio.astype(np.int16)
        play_obj = sa.play_buffer(audio, 1, 2, fs)
    play_obj.wait_done()

freca = [123,230,400,500]
reproduce_frecuencia(freca,3)
