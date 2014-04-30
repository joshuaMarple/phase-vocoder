from app import insertSpaces
from app import pitchMod
from app import durMod
from app import soundMod
from lib import tgt

class Sound:
    def __init__(self, soundPath, textgridPath):
        self.soundPath = soundPath
        self.textgrid = tgt.read_textgrid(textgridPath)
    def pauseInsertion(self, index, duration):
        """
        Input: index, duration
        index(Int): The index of the word to add time before
        duration(float): The duration of the silence to insert
        Description: Inserts silence before a word at the given index
        """
        wordTier = self.textgrid.get_tier_by_name('words')
        if index == 0:
            silenceStart = 0
        else:
            wordIntervals = filter(lambda x: x.text != "sil" and x.text != "sp", wordTier)
            silenceStart = wordIntervals[index-1].end_time
        
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
        pass

    def intensityMod(self, startTime, length, decibels):
        '''
        We'll need to talk about what parameters to  pass
        to this one too. It will call soundMod from
        soundMod.py.
        '''
        pass

    def durMod(self, startTime, length, percentage):
      '''
      Input: percentage
      startTime(Float): the beginning of the sound interval to have its tempo(and duration) changed (in seconds)
      length (float): the size of the interval to be changed (in seconds)
      percentage (float) : Changes the tempo of a sound file based in a percentage where -50 % increases the sound time and 50% diminishes (a faster/bigger tempo diminishes sound time, a smaller/slower tempo increases sound time) 
      Description: Changes the tempo of a sound file, consequently changing its duration whithout changing the pitch
      '''
      durMod.changeGapDuration(self.soundPath, startTime, length, percentage)
      pass
    
        
      
if __name__ == "__main__":ter
    s = Sound("example.wav", "example.TextGrid")
    s.pauseInsertion(1,1)
