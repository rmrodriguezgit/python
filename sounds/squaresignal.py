from scipy import signal
import matplotlib.pyplot as plot
import numpy as np

#https://www.geeksforgeeks.org/plotting-a-square-wave-using-matplotlib-numpy-and-scipy/

t = np.linspace(0, 1, 1000, endpoint=True)
#freq = 17000
freq = input('Frecuencia: ')
plot.plot(t, signal.square(2 * np.pi * float(freq) * t))

plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.title('Square wave - Geeksforgeeks')

plot.axhline(y = 0, color = 'k')

plot.show()
