import subprocess
import os
from sys import platform as _platform

def changePitch(filename,tones):
  """
  Input: n
  n (integer): the number to do the factorial function on
  Returns: The value of n!
  Description: This function will return n!
  """
  pitchchange = "-pitch="+str(tones)
  if _platform == "linux" or _platform == "linux2":
    fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'soundpitch')
  elif _platform == "darwin":
    fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'soundpitchmac')
  elif _platform == "win32":
    fn = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'soundpitchwin32.exe')

  subprocess.call([fn,filename, "pitchoutput.wav","-speech", pitchchange])
  #self.nsound=SndTable("temp_outvoice.aif")
  #self.nsound.save("outputfinal.wav", 0, 0)
  #os.remove( os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp_outvoice.aif') )
  #os.remove( os.path.join(os.path.abspath(os.path.dirname(__file__)), 'temp_voice.aif') )
  #print fn

changePitch("example.wav", 4)




