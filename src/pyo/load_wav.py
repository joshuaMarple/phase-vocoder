import pyo
import time

path = "example.wav"
frames, duration, sampRate, channels, fileFormat, sampType = pyo.sndinfo(path)

server = pyo.Server()
server.boot()
print("booted server")
server.start()

sound = pyo.SfPlayer(path).out()
soundHigh = pyo.FreqShift(sound, shift = 1000)
soundLow = pyo.FreqShift(sound, shift = -1000)
soundQuiet = sound * .6
soundLoud = sound / .6
rec = pyo.Record(sound, "test.wav")
recHigh = pyo.Record(soundHigh, "example_high.wav")
recLow = pyo.Record(soundLow, "example_low.wav")
recQuiet = pyo.Record(soundQuiet, "example_quiet.wav")
recLoud = pyo.Record(soundLoud, "example_loud.wav")
print("start recording...")
time.sleep(duration)
print("stop recording.")
rec.stop()
recHigh.stop()
recLow.stop()
recQuiet.stop()
recLoud.stop()
