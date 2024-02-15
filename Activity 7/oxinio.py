from thinkdsp import SawtoothSignal
from thinkdsp import decorate

signal = SawtoothSignal(30)
duration = signal.period*3
segment = signal.make_wave(duration, framerate=10000)
segment.plot()
decorate(xlabel='Time (s)')
wave = signal.make_wave(duration=3.5, framerate=10000)
wave.apodize()
wave.make_audio()
