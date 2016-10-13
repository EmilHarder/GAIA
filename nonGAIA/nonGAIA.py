#!/usr/bin/python3 -B

#This is version number 2. Lest call this one for 0.1a. With subsequinding .n, for the n'th number of alpha.

"""
     ___________________________________________________________________
    |					              			|
    |	  ________	 __________	 __________	 __________ 	|
    |	 /   ___  \	|	   |	|	   |	|	   |	|
    |   |   /   \__|	|   ____   |	|__      __|	|   ____   |	|
    |	|  |		|  |    |  |	   |    |	|  |    |  |	|
    |	|  |   ____	|  |____|  |	   |    |	|  |____|  |	|
    |	|  |  |_   |	|   ____   |	   |    |	|   ____   |	|
    |	|  |    |  |	|  |	|  |	   |    |   	|  |	|  |	|
    |	|   \___/  |	|  |	|  |	 __|    |__ 	|  |	|  |	|
    |	|	   |	|  |	|  |	|	   |	|  |	|  |	|
    |non \________/	|__|	|__|	|__________|	|__|	|__|	|
    |								   	|
    |			            	Vers. 0.1a.2			|
    |___________________________________________________________________|

This module holds (when finished) a start screen of some kind.
A possibility to choose between running a existing preset, making a new setup or a single instance.
And thats it.

"""

"""
Modules
"""

#First there is the importing of external modules:
import subprocess
import time
import os

#Next the module with functions for nonGAIA:
import GAIAFunc

"""
Setting the working directory in the users home folder, if not already present
"""

#Get the home directory
homeDir = os.getenv("HOME")

#Check if the folder .GAIA exist
GAIADirExist = os.path.isdir("%s/.GAIA" % (homeDir))

if GAIADirExist == True:

#Then change dir to .GAIA
	os.chdir("%s/.GAIA" % (homeDir))

elif GAIADirExist == False:

#Else create it, and change to it
	os.makedirs("%s/.GAIA" % (homeDir))
	os.chdir("%s/.GAIA" % (homeDir))

else:

#Or at last tell that theres something wrong
	print("Something is completely wrong, in creating a working directory in your home folder.")

GAIADir = "%s/.GAIA" % (homeDir)

#Check if the preset directory exist
presetDirExist = os.path.isdir("%s/Presets" % (GAIADir))

if presetDirExist == True:

#Then change dir to .GAIA
	os.chdir("%s/Presets" % (GAIADir))

elif presetDirExist == False:

#Else create it, and change to it
	os.makedirs("%s/Presets" % (GAIADir))
	os.chdir("%s/Presets" % (GAIADir))

else:

#Or at last tell that theres something wrong
	print("Something is completely wrong, in creating the preset directory in ~/.GAIA.")


#Now the time has come to the welcome
print("Welcome to nonGAIA!\nThe nonGraphical Audio Interface Aggregation\n\nThe possibility to aggregate audio interfaces in a (hopefully) user friendly way.\nThank you for using this script!\n")

#The user can choose between activating an existing preset, make a new setup or quit.
chooseStart = input("Do you want to use an existing preset (1), make a new preset to run (2), running a single instance (3) or quit (already) (4)? ")

#A while loop for controlling the input of chooseStart is made
chooseStartLoop = True
while chooseStartLoop:

#If the user wants to use an existing preset, the function for choosing preset is called 
	if chooseStart == "1":

		GAIAFunc.choosePre(homeDir)
		chooseStartLoop = False

#If the user wants to make a new preset, the function for that will be called.
	elif chooseStart == "2":

		GAIAFunc.newSetup()
		chooseStartLoop = False

#If the user wants to run a singe instance, that function will be called.
	elif chooseStart == "3":

		print("\nTo be written.... (GAIAFunc.singleInstance) \n")
		chooseStartLoop = False

#Lastly if the user wants to quit-, quit.
	elif chooseStart == "4":

		print("\nBye then.. \n")
		chooseStartLoop = False

#If the use fails in choosing between 1 and 2, they gets to here
	else:

		chooseStart = input("Please answer either '1', '2', '3' or '4'. ")
		chooseStartLoop = True

#Sleep tight
