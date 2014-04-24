import nltk.textgrid

class Sound:
    def __init__(self, soundPath, textgridPath):
        self.soundPath = soundPath
        self.textgrid = textgrid.TextGrid.load(textgridPath)
    def addSilenceAfterWord(self, index):
        pass
