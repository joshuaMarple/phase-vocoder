""" 
Authors: Perry Gowdy (pgowdy1@gmail.com)
License: GPL 3.0
Description: This file contains a function that allows the user to 
change volume of a .wav file at specific segments
Comments: None.
"""

from lib import pydub

"""
Input: filename , gaptime, gaplength, decibel 
filename (string): the path to the soundfile
gaptime (float): the time to begin changing the volume
gapduration (float): the amount of time that sound will be changed(from the gaptime start to the end of this length)
decibel (integer): the number of decibels to chang ethe volume by(from negative number to positive number) 
Outputs: processefile.wav
Description: This function will change the volume of a soundfile
"""

def changeVolume(filename, gaptime, gaplength, decibel):
    file = pydub.AudioSegment.from_wav(filename)
    segment = file[int((gaptime* 1000)) : int(((gaptime+gaplength) * 1000))]
    segment = segment + decibel
    first = file[:int(gaptime * 1000)]
    last = file[int((gaptime+gaplength) * 1000):]
    newfile = first + segment + last
    newfile.export(filename, format="wav")
    return newfile
