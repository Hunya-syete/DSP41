#9.1

import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal, Wave


triangle_signal = TriangleSignal(freq=440)

wave = triangle_signal.make_wave(duration=0.01)

wave.plot()
plt.show()
spectrum = wave.make_spectrum()
print("Amplitude of component with frequency 0:", spectrum.hs[0])
print("Phase of component with frequency 0:", spectrum.angles[0])

spectrum.hs[0] = 100
wave_modified = spectrum.make_wave()

wave_modified.plot()
plt.show()

#9.2


from thinkdsp import Chirp

class SawtoothChirp(Chirp):
    
    
    def evaluate(self, ts):
        freqs = np.linspace(self.start, self.end, len(ts))
        dts = np.diff(ts, prepend=0)
        dphis = 2 * np.pi * freqs * dts
        phis = np.cumsum(dphis)
        ys = np.mod(phis, 2 * np.pi) / (2 * np.pi)
        ys = ys * 2 - 1
        return ys
sawtooth_chirp = SawtoothChirp(start=220, end=880)
wave_chirp = sawtooth_chirp.make_wave(duration=1)
wave_chirp.plot()
plt.show()
wave_chirp.make_spectrogram(1024).plot()
plt.show()
