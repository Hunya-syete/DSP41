9.1
import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal, Wave

# 1. Make a triangle signal with frequency 440 and make a Wave with duration 0.01 seconds. Plot the waveform.
triangle_signal = TriangleSignal(freq=440)
wave = triangle_signal.make_wave(duration=0.01)
wave.plot()
plt.title("Triangle Waveform (440 Hz)")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

# 2. Make a Spectrum object and print spectrum.hs[0]. What is the amplitude and phase of this component?
spectrum = wave.make_spectrum()
print("Amplitude of component with frequency 0:", spectrum.hs[0])
print("Phase of component with frequency 0:", spectrum.angles[0])

# 3. Set spectrum.hs[0] = 100. Make a Wave from the modified Spectrum and plot it. What effect does this operation have on the waveform?
spectrum.hs[0] = 100
wave_modified = spectrum.make_wave()
wave_modified.plot()
plt.title("Modified Waveform")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

9.2
from thinkdsp import Chirp

class SawtoothChirp(Chirp):
    """A class that extends Chirp to generate a sawtooth waveform with linearly increasing (or decreasing) frequency."""
    
    def evaluate(self, ts):
        """Override the evaluate function to generate a sawtooth waveform."""
        # Compute the frequency at each time point
        freqs = np.linspace(self.start, self.end, len(ts))
        # Compute the phase shift at each time point
        dts = np.diff(ts, prepend=0)
        dphis = 2 * np.pi * freqs * dts
        phis = np.cumsum(dphis)
        # Generate the sawtooth waveform
        ys = np.mod(phis, 2 * np.pi) / (2 * np.pi)
        ys = ys * 2 - 1
        return ys

# Instantiate the SawtoothChirp
sawtooth_chirp = SawtoothChirp(start=220, end=880)
# Make a wave with duration 1 second
wave_chirp = sawtooth_chirp.make_wave(duration=1)
# Plot the waveform
wave_chirp.plot()
plt.show()

# Plot the spectrogram
wave_chirp.make_spectrogram(1024).plot()
plt.show()
