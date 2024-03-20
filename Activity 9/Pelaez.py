import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
frequency = 440  # Hz
duration = 0.01  # seconds
sample_rate = 44100  # Hz

# Time array
t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)

# Generate triangle signal
triangle_wave = signal.sawtooth(2 * np.pi * frequency * t, width=0.5)

# Plot the waveform
plt.plot(t, triangle_wave)
plt.title('Triangle Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal, Wave, decorate

# Parameters
frequency = 440  # Hz
duration = 0.01  # seconds
sample_rate = 44100  # Hz

# Create triangle signal
triangle = TriangleSignal(freq=frequency)
wave = triangle.make_wave(duration=duration, framerate=sample_rate)

# Create Spectrum object
spectrum = wave.make_spectrum()

# Print the first component
print("Amplitude of the first component:", spectrum.hs[0])
print("Phase of the first component (radians):", np.angle(spectrum.hs[0]))

# Plot the spectrum
spectrum.plot()
decorate(xlabel='Frequency (Hz)', ylabel='Amplitude')

plt.show()

import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal, Wave, decorate

# Parameters
frequency = 440  # Hz
duration = 0.01  # seconds
sample_rate = 44100  # Hz

# Create triangle signal
triangle = TriangleSignal(freq=frequency)
wave = triangle.make_wave(duration=duration, framerate=sample_rate)

# Create Spectrum object
spectrum = wave.make_spectrum()

# Set the amplitude of the first component to 100
spectrum.hs[0] = 100

# Make a wave from the modified spectrum
modified_wave = spectrum.make_wave()

# Plot the modified waveform
modified_wave.plot()
decorate(xlabel='Time (s)', ylabel='Amplitude')

plt.show()

from thinkdsp import Chirp

signal = Chirp(start=220, end=880)
wave1 = signal.make_wave(duration=15)
wave1.make_audio()
signal = Chirp(start=220, end=440)
wave1 = signal.make_wave(duration=1)
spectrum = wave.make_spectrum()
wave1.segment(start=0, duration=0.01).plot()
decorate(xlabel='Time (s)')
from thinkdsp import ExpoChirp

signal = ExpoChirp(start=220, end=880)
signal2 = ExpoChirp(start=880, end=220)
wave2 = signal.make_wave(duration=15)
wave2 = signal2.make_wave(duration=15)
wave2.make_audio()
