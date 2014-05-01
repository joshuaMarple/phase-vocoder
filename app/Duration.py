import subprocess
import os
from sys import platform as _platform
from lib import pydub

def changeDuration(filename,percent):
  """
  Input: filename , tones
  filename (string): the path to the soundfile
  tones (integer): the number of semitones to change(from negative number to positive number)
  Outputs: pitchoutput.wav
  Description: This function will change the pitch of a soundfile
  """
  tempochange = "-tempo="+str(percent)
  if _platform == "linux" or _platform == "linux2":
    fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'soundpitch')
  elif _platform == "darwin":
    fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'soundpitchmac')
  elif _platform == "win32":
    fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'soundpitchwin32.exe')

  subprocess.call([fn,filename, "duroutput.wav","-speech", tempochange])
  
  return "duroutput.wav"
  

def changeGapDuration(filename,gaptime,gapduration,percentage):
  """
  Input: filename , gaptime, gapduration , tones
  filename (string): the path to the soundfile
  gaptime (float): the time to begin changing the pitch
  gapduration (float): the amount of sound to be changed(from the gaptime start to the end of this length)
  tones (integer): the number of semitones to change(from negative number to positive number) 
  Outputs: processefile.wav
  Description: This function will change the pitch of a soundfile
  """
  file = pydub.AudioSegment.from_wav(filename)
  newdurationpart = file[int((gaptime* 1000)) : int(((gaptime+gapduration) * 1000))]
  first = file[:int(gaptime * 1000)]
  last = file[int((gaptime+gapduration) * 1000):]
  newdurationpart.export("durinput.wav", format="wav")
  changeDuration("durinput.wav",percentage)
  newdurationpart = pydub.AudioSegment.from_wav("duroutput.wav")
  newfile = first + newdurationpart + last
  newfile.export(filename, format="wav")
  
  os.remove("durinput.wav")
  os.remove("duroutput.wav")
  
  return newfile




