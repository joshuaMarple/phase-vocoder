import pydub

def insertSilence(filename, gaptime, gaplength):
	import pydub
	file = pydub.AudioSegment.from_wav(filename)
	silence = file[:gaplength * 1000]
	silence = silence - 50000
	first = file[:gaptime * 1000]
	last = file[gaptime * 1000:]
	newfile = first + silence + last
	newfile.export("processedfile.wav", format="wav")
	return newfile