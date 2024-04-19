import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
sample_rate = 44100 
freq = 600 
duration = 10 
t = np.linspace(0, duration, sample_rate * duration, False)
note = np.sin(freq * t * 50 * np.pi)
plt.figure(figsize=(20, 4))
plt.plot(t[:1000], note[:1000])
plt.show()
audio = Audio(note, rate=sample_rate)
audio
