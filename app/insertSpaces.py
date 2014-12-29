""" 
Authors: Joshua Marple (marpljos@gmail.com)
License: GPL 3.0
Description: This file contains functions that allows the user to 
insert silence into a .wav file 
Comments: None.
"""

from lib import pydub


"""
Input: filename , gaptime, gaplength, 
filename (string): the path to the soundfile
gaptime (float): the time to begin inserting silence
gapduration (float): the amount of time that sound will be changed(from the gaptime start to the end of this length) 
Outputs: processefile.wav
Description: This function will insert silence into a .wav file 
"""
def insertSilence(filename, gaptime, gaplength):
	file = pydub.AudioSegment.from_wav(filename)
	silence = file[:int(gaplength * 1000)]
	silence = silence - 50000 # arbitrary number, makes it very very quiet
	first = file[:int(gaptime * 1000)]
	last = file[int(gaptime * 1000):]
	newfile = first + silence + last
	newfile.export(filename, format="wav")
