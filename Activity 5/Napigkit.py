import numpy as np
from IPython.display import Audio, display

duration, sampling_freq, frequency = 0.5, 48000, 440.0

t = np.arange(0, duration, 1/sampling_freq)
sound_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

display(Audio(data=sound_wave, rate=sampling_freq))
