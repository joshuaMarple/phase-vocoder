from app import insertSpaces
from app import pitchMod
from app import durMod
from app import soundMod
from app import changeVolume
from lib import tgt

class Sound:
    def __init__(self, soundPath, textgridPath):
        self.soundPath = soundPath
        self.textgrid = tgt.read_textgrid(textgridPath)
        self.textgridPath = textgridPath
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
            # Shift all later intervals
            for interval in tier:
                if interval.start_time > silenceStart:
                    interval.end_time += duration
                    interval.start_time += duration
            
        tier.get_annotation_by_start_time(silenceStart).end_time += duration

        # Save grid
        tgt.write_to_file(self.textgrid, self.textgridPath, format = "long")

    def pitchMod(self, startTime, length, shift):
        '''
        Input: startTime,length,shift
        startTime(Float): the beginning of the sound interval to have its pitch changed (in seconds)
        length (float): the size of the interval to be changed (in seconds)
        shift (integer): the amount of semitones to change the pitch (can be a positive number [to make pitch higher] or a negative number[to make pitch lower])
        Description: Changes the pitch of a sound without changing its duration
        '''
        pitchMod.changeGapPitch(self.soundPath,startTime,length,shift)
        pass

    def intensityMod(self, startTime, length, decibels):
        '''
        Input: startTime, length, decibels
        startTime(Float): the beginning of the sound interval to have its volume changed (in seconds)
        length(Float): the size of the interval to be change (in seconds)
        decibels(Float): the number of decibels to increase the volume by (or decrease if negative)
        Description: Changes the volume of an interval of a sound file
        '''
        changeVolume.changeVolume(self.soundPath, startTime, length, decibels)

    def durMod(self, startTime, length, percentage):
        '''
        Input: percentage
        startTime(Float): the beginning of the sound interval to have its tempo(and duration) changed (in seconds)
        length (float): the size of the interval to be changed (in seconds)
        percentage (float) : Changes the tempo of a sound file based in a percentage where -50 % increases the sound time and 50% diminishes (a faster/bigger tempo diminishes sound time, a smaller/slower tempo increases sound time) 
        Description: Changes the tempo of a sound file, consequently changing its duration whithout changing the pitch
        '''
        # durMod.changeGapDuration(self.soundPath, startTime, length, percentage)
  
        # Adjust time in textgrid
        for tier in self.textgrid:
            print("processing tier")
            # Shift all later intervals
            prevEndTime = 0
            for interval in tier:
                print("processing interval")
                shift = prevEndTime - interval.start_time
                interval.start_time += shift
                interval.end_time += shift
                
                # How much of the sound whose duration is being changed
                # is in this interval?
                thisIntervalStart = max(interval.start_time, startTime)
                thisIntervalEnd = min(interval.end_time, startTime + length)
                timeThisInterval = thisIntervalEnd - thisIntervalStart
  
                if timeThisInterval > 0:
                    lengthChange = (timeThisInterval * percentage / 100) - timeThisInterval
                    interval.end_time += lengthChange
                prevEndTime = interval.end_time
            
        # Save grid
        tgt.write_to_file(self.textgrid, "out.TextGrid", format = "long")
      
if __name__ == "__main__":
    s = Sound("example.wav", "example.TextGrid")
    s.durMod(1, .5, 50)
