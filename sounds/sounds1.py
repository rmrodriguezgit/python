from sksound.sounds import Sound
import numpy as np
#mySound1 = Sound()                  # here the user is prompted for an input file
#mySound2 = Sound('test.wav')     # here the input file is provided directly

rate = 22050
dt = 1./rate
#freq = 440
freq = input('Frecuencia: ')
t = np.arange(0,0.5,dt)
x = np.sin(2*np.pi*float(freq) * t)
amp = 2**13
sounddata = np.int16(x*amp)
mySound3 = Sound(inData=sounddata, inRate=rate)


mySound3.play()
