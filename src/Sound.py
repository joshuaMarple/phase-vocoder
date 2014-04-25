import tgt
import insertSpaces
import pitchMod
import soundMod

class Sound:
    def __init__(self, soundPath, textgridPath):
        self.soundPath = soundPath
        self.textgrid = tgt.read_textgrid(textgridPath)
    def pauseInsertion(self, index, length):
        """
        This will get the time of the end of the word from
        the textgrid file, insert the silence at that point
        in the wave file using insertSpaces, and rewrite
        the textgrid file to reflect the change.
        """
        startTime = self.textgrid.get_tier_by_name('words')[0]

    def pitchMod(self, startTime, length, shift):
        '''
        We'll need to talk about what parameters to
        pass this one. It will call pitchMod that is
        defined in pitchMod.py
        '''
        pass

    def intensityMod(self, startTime, length, decibels):
        '''
        We'll need to talk about what parameters to  pass
        to this one too. It will call soundMod from
        soundMod.py.
        '''
        pass

    def durMod(self, soundIndex, newDuration):
        '''
        We haven't talked about how to implement this one.
        '''
        pass
