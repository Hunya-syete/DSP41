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
