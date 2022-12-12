import numpy as np
from waves import Sound

duration, fps, frequencies, volume = (3, 44100, (110, 440), 0.5)
amplitude = np.iinfo(np.int16).max * volume

def time_to_frame(t):
    return [
        (np.sin(frequencies[0] * 2 * np.pi * t) * amplitude).astype(np.int16),
        (np.sin(frequencies[1] * 2 * np.pi * t) * amplitude).astype(np.int16),
    ]

sound = Sound.from_datatimes(time_to_frame, fps=fps).with_duration(duration)
sound.play()
