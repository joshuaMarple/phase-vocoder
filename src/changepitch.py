import subprocess
import os
from sys import platform as _platform

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





