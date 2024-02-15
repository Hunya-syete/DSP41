from thinkdsp import SawtoothSignal
from thinkdsp import decorate

signal = SawtoothSignal(1)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=990000)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=0.5, framerate=100000)
wave.apodize()
wave.make_audio()
