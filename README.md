phase-vocoder
=============

Phase Vocoding Specification
The purpose of this document is to outline what all will need to be implemented into the phase vocoder. Due dates will be provided at a later date via a google calendar.

END GOAL:
The end goal of this project will be to take a sound file with speech inside it, along with a file called a text grid file, and then be able to arbitrarily change the pitch, duration, pauses, and intensity of words inside of it. When these get accomplished, we would also like to be able to have it change the pitch automatically at the end of a sentence depending on whether it is a statement or a question.

So, it will need to be a module that implements these functions:

loadFile(soundFile, textGridFile):
loads the above files, and begins some initial processing upon them

pitchMod(time or word or vowel):
changes the pitch of words/vowels at specific times, specific words, or specific vowels (consonants cannot be changed, for reasons)

durMod(time or word or vowel):
changes the duration of words/vowels at specific times, words, or vowels (consonants cannot be changed, for reasons)

pauseInsertion(time or word):
Inserts a pause at a specific time or after a specific word

intensityMod(time or word or vowel):
changes the intensity at a specific time or of a word or vowel

Sound hard? Don’t worry, it won’t be. Most of our work will use the PYO Library. What we need to do is wrap these functions in a way that makes it easy for someone using this library. 

Similarly, there is a library called tgt that can be installed using pip. This library has a number of tools that will make it very easy to open up and use text grid files (the second part of that input). 

So, in conclusion, we have a priority of tasks to accomplish.
-investigating each of these libraries and seeing how they work
-implementing file loading and changes in directories
-changing pitch of tones
-changing duration of tones
-inserting pauses
-changes in intensity

Our inputs will be a sound file and a text grid file.
Our outputs will be a sound file, and a new modified text grid file.
