#Author: Perry Gowdy
#License: Open
#Description: A program that changes the pitch of a wav file
#Comments: Make sure to be careful about including filetypes when asking
# for names. You must include .wav
################################################################################


import wave

################################################################################
#Pitch Change Function
#Input: fileName = string, changeInPitch = num 
#Returns: 
#Description: The function will take in a .wav file and output a
# file with a modified pitch. You can choose how much to modify the
# pitch and the name of the output file
################################################################################
    
def pitchChange(fileName, changeInPitch):
    
    CHANNELS = 1
    swidth = 2

    wavStreamIn = wave.open(fileName, 'rb')
    RATE = wavStreamIn.getframerate()
    print "Your sample rate is: ", RATE
    signal = wavStreamIn.readframes(-1)
    
    output = raw_input('What would you like the output file to be named (include the filetype (example: .wav) at the end)? ')
    wavStreamOut = wave.open(output, 'wb')
    wavStreamOut.setnchannels(CHANNELS)
    wavStreamOut.setsampwidth(swidth)
    wavStreamOut.setframerate(RATE*changeInPitch)
    wavStreamOut.writeframes(signal)
    wavStreamOut.close()
        



