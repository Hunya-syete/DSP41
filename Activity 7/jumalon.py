import os
from thinkdsp import SawtoothSignal
from thinkdsp import decorate

signal = SawtoothSignal(400)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=2, framerate=10000)
wave.apodize()
wave.make_audio()
