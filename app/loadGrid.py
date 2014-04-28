# import nltk
import textgrid
import sys
import os.path

if len(sys.argv) == 1:
    raise IOError("Syntax: load_grid.py filename")
else:
    path = sys.argv[1]

if not(os.path.isfile(path)):
    raise IOError("File {} was not found".format(path))

t = textgrid.TextGrid.load(path)
tier = t.tiers[0]
print(tier.simple_transcript)


