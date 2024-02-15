import os

if not os.path.exists('thinkdsp.py'):
    !wget https://github.com/AllenDowney/ThinkDSP/raw/master/code/thinkdsp.py

from thinkdsp import TriangleSignal
from thinkdsp import decorate

signal = TriangleSignal(50)
duration = signal.period*2
segment = signal.make_wave(duration, framerate=20000)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')

from thinkdsp import SquareSignal

signal = SquareSignal(300)
duration = signal.period*2
segment = signal.make_wave(duration, framerate=30000)
segment.plot()
decorate(xlabel='Time (s)')

wave = signal.make_wave(duration=0.5, framerate=10000)
wave.apodize()
wave.make_audio()

spectrum = wave.make_spectrum()
spectrum.plot()
decorate(xlabel='Frequency (Hz)')





