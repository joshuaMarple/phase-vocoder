from lib import pydub

def changeVolume(filename, gaptime, gaplength, decibel):
    file = pydub.AudioSegment.from_wav(filename)
    segment = file[:int(gaplength * 1000)]
    segment = segment + decibel
    first = file[:int(gaptime * 1000)]
    last = file[int(gaptime * 1000):]
    newfile = first + segment + last
    newfile.export("processedfile.wav", format="wav")
    return newfile
