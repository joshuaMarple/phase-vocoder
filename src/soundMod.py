import pydub

def changeVolume(filename, decibel):
    import pydub
    file = pydub.AudioSegment.from_wav(filename)
    newfile = file + decibel
    newfile.export("processedfile.wav", format="wav")
    return newfile
