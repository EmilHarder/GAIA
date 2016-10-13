#!/usr/bin/python -B

#This is version number 2. Lest call this one for 0.1a.

"""
     ___________________________________________________________________
    |									|
    |	  ________	 __________	 __________	 __________	|
    |	 /   ___  \	|	   |	|	   |	|	   |	|
    |   |   /   \__|	|   ____   |	|__      __|	|   ____   |	|
    |	|  |		|  |    |  |	   |    |	|  |    |  |	|
    |	|  |   ____	|  |____|  |	   |    |	|  |____|  |	|
    |	|  |  |_   |	|   ____   |	   |    |	|   ____   |	|
    |	|  |    |  |	|  |	|  |	   |    |	|  |	|  |	|
    |	|   \___/  |	|  |	|  |	 __|    |__	|  |	|  |	|
    |	|	   |	|  |	|  |	|	   |	|  |	|  |	|
    |	 \________/	|__|	|__|	|__________|	|__|	|__|	|
    |									|
    |				Vers. 0.1a				|
    |___________________________________________________________________|

This module holds (when finished) a start screen of some kind.
A possibility to choose between running a existing preset or making a new setup.
And thats it. One module per function. Hopefully thats a advantage when the graphical part comes in.

"""

#First there is the importing of external modules:
import subprocess
import time
import os

#Next the other modules of GAIA:
import GAIAFunc

#Setting the working directory in the users home folder, if not already present
#Get the home directory

homeDir = os.getenv("HOME")

GAIADirExist = os.path.isdir("%s/.GAIA" % (homeDir))

if GAIADirExist == True:

	os.chdir("%s/.GAIA" % (homeDir))

elif GAIADirExist == False:

	os.makedirs("%s/.GAIA" % (homeDir))
	os.chdir("%s/.GAIA" % (homeDir))

else:

	print("Something is completely wrong, in creating a working directory in your home folder.")

GAIADir = "%s/.GAIA" % (homeDir)

#Now the time has come to the welcome
print("\nWelcome to nonGAIA!\nThe nonGraphical Audio Interface Aggregation\n\nThe possibility to aggregate audio interfaces in a (hopefully) user friendly way.\nThank you for using this script!\n")

#The user can choose between activating an existing preset or make a new setup.
chooseStart = raw_input("Do you want to use an existing preset (1), or make a new setup (2)? ")

#A loop begins to make the choice in
chooseStartLoop = True
while chooseStartLoop:

	if chooseStart == "1":

#If the user wants to use an existing preset, the module and function for choosing preset is called 
		print("")
		GAIAFunc.choosePre(homeDir)
		chooseStartLoop = False

	elif chooseStart == "2":

#If the user wants to make a new setup, and possibly save it as a preset, the modules for that will be loaded here.
		print("")
#		GAIAFunc.
		chooseStartLoop = False

	else:

#If the use fails in choosing between 1 and 2, they gets to here
		chooseStart = raw_input("Please answer either '1' or '2'. ")
		chooseStartLoop = True

#Now its time to activate the choosen setup with actPre
GAIAFunc.actSetup(homeDir, GAIADir)

#At last we have to stop zita
GAIAFunc.stopZita()

#Sleep tight
