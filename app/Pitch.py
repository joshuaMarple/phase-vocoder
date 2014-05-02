""" 
Authors: Fernando (UPDATE HIS INFO)
License: GPL 3.0
Description: This file contains functions that allows the user to 
change the pitch of a .wav 
Comments: None.
"""

import subprocess
import os
from sys import platform as _platform
from lib import pydub

def changePitch(filename,tones):
  """
  Input: filename , tones
  filename (string): the path to the soundfile
  tones (integer): the number of semitones to change(from negative number to positive number)
  Outputs: pitchoutput.wav
  Description: This function will change the pitch of a soundfile
  """
  pitchchange = "-pitch="+str(tones)
  if _platform == "linux" or _platform == "linux2":
    fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'soundpitch')
  elif _platform == "darwin":
    fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'soundpitchmac')
  elif _platform == "win32":
    fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'soundpitchwin32.exe')

  subprocess.call([fn,filename, "pitchoutput.wav","-speech", pitchchange])
  
  return "pitchoutput.wav"

 
def changeGapPitch(filename,gaptime,gaplength,tones):
  """
  Input: filename , gaptime, gaplength , tones
  filename (string): the path to the soundfile
  gaptime (float): the time to begin changing the pitch
  gaplength(float): the amount of sound to be changed(from the gaptime start to the end of this length)
  tones (integer): the number of semitones to change(from negative number to positive number) 
  Outputs: processefile.wav
  Description: This function will change the pitch of a soundfile
  """
  file = pydub.AudioSegment.from_wav(filename)
  newpitchpart = file[int((gaptime* 1000)) : int(((gaptime+gaplength) * 1000))]
  first = file[:int(gaptime * 1000)]
  last = file[int((gaptime+gaplength) * 1000):]
  newpitchpart.export("pitchinput.wav", format="wav")
  changePitch("pitchinput.wav",tones)
  newpitchpart = pydub.AudioSegment.from_wav("pitchoutput.wav")
  newfile = first + newpitchpart + last
  newfile.export(filename, format="wav")
  
  os.remove("pitchinput.wav")
  os.remove("pitchoutput.wav")





