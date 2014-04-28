from app import insertSpaces
from app import pitchMod
from app import soundMod
from app import changePitch
from app import loadGrid

class Sound:
    def __init__(self, soundPath, textgridPath):
        self.soundPath = soundPath
        self.textgrid = tgt.read_textgrid(textgridPath)
    def pauseInsertion(self, index, duration):
        """
        This will get the time of the end of the word from
        the textgrid file, insert the silence at that point
        in the wave file using insertSpaces, and rewrite
        the textgrid file to reflect the change.
        """
        wordTier = self.textgrid.get_tier_by_name('words')
        wordIntervals = filter(lambda x: x.text != "sil" and x.text != "sp", wordTier)
        silenceStart = wordIntervals[index].end_time
        
        # insert silence into wave
        # insertSpaces.insertSilence(self.soundPath, silenceStart, duration)
        
        # insert silence into textgrid
        for tier in self.textgrid:
            print("processing tier")
            # Shift all later intervals
            for interval in tier:
                print("processing interval")
                if interval.start_time > silenceStart:
                    interval.end_time += duration
                    interval.start_time += duration
            
        tier.get_annotation_by_start_time(silenceStart).end_time += duration

        # Save grid
        tgt.write_to_file(self.textgrid, "out.TextGrid", format = "long")

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

if __name__ == "__main__":
    s = Sound("example.wav", "example.TextGrid")
    s.pauseInsertion(1,1)
