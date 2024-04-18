import os
import numpy as np
import matplotlib.pyplot as plt 
from IPython.display import Audio

def stretched(wave, stretch_factor, sample_rate):
    new_wave = np.interp(t, t, wave) * stretch_factor
    new_t = t / stretch_factor
    new_sample_rate = sample_rate / stretch_factor
    return new_wave, new_t, new_sample_rate

duration = 5.0
sampling_freq = 44100
frequency = 600.0

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

stretch_factor = 4
new_wave, new_t, new_sample_rate = stretched(sound_wave, stretch_factor, sampling_freq)

plt.plot (new_t, new_wave)
plt.title ('Stretched Sine Wave')
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

audio = Audio(new_wave, rate = new_sample_rate)
display(audio)
