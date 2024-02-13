import os

if not os.path.exists('thinkdsp.py'):
    !wget https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py
import numpy as np
import matplotlib.pyplot as plt 
from IPython.display import Audio

duration = 5.0
sampling_freq = 44100
frequency = 10


t = np.arange(0, duration, 1/ sampling_freq)

sound_wave = np.sin(2* np.pi * frequency * t )

plt.plot (t, sound_wave)
plt.title ('Simple Sine Wave')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

audio = Audio(sound_wave, rate = sampling_freq)
display(audio)
