import numpy as np
import matplotlib.pyplot as plt

# Parameters
duration = 1.0  # seconds
sampling_freq = 44100  # Hz
freq = 440  # Hz (frequency of the sine wave)

# Generate time array
t = np.linspace(0, duration, int(sampling_freq * duration), endpoint=False)

# Generate sine wave
waveform = np.sin(2 * np.pi * freq * t)

# Plot
plt.plot(t, waveform)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Simple Sine Wave')
plt.grid(True)
plt.show()
