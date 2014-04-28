from app import insertSpaces
from app import pitchMod
from app import durMod
from app import soundMod

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
        insertSpaces.insertSilence(self.soundPath, silenceStart, duration)
        
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
        tgt.write_to_file(self.textgrid, self.textgrid, format = "long")

    def pitchMod(self, startTime, length, shift):
       '''
        Input: starTime,length,shift
        startTime(Float): the beginning of the sound interval to have its pitch changed (in seconds)
        length (float): the size of the interval to be changed (in seconds)
        shift (integer): the amount of semitones to change the pitch (can be a positive number [to make pitch higher] or a negative number[to make pitch lower])
        Description: Changes the pitch of a sound without changing its duration
        '''
        pitchMod.changeGapPitch(self.soundPath,startTime,length,shift)

    def intensityMod(self, startTime, length, decibels):
        '''
        We'll need to talk about what parameters to  pass
        to this one too. It will call soundMod from
        soundMod.py.
        '''
        pass

     def durMod(self, percentage):
        '''
        Input: percentage
        percentage (integer) : Changes the tempo of a sound file based in a percentage where -50 % doubles the sound time and 50% half it
        Description: Changes the duration of a sound file whithout changing the pitch
        '''
        durMod.changeDuration(self.soundPath,percentage)
        pass

if __name__ == "__main__":
    s = Sound("example.wav", "example.TextGrid")
    s.pauseInsertion(1,1)
