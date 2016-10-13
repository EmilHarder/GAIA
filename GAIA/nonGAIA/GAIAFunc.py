#!/usr/bin/python -B

#First there is the importing of external modules:
import subprocess
import time
import os

"""
Choose Preset
"""

#The function begins

def choosePre(x):

	global setupToActivate

	homeDir = x

#Then make a list of the stored files (presets) in the preset folder in .GAIA

#First the directory for presets has to be set
#A check to see if the directory for presets exist, if not, make it

	if ("%s/.GAIA/Presets" % (homeDir)) == False:

		os.makedirs("%s/.GAIA/Presets" % (homeDir))

#Now a var can be set for the preset directory
	presetDir = "%s/.GAIA/Presets" % (homeDir)

#And the files in the directory have to get sorted
	files = sorted(os.listdir("%s/.GAIA/Presets" % (homeDir)))

#Soted list of presets can be shown with numbers in front, tada!
#Didn't think I would survive that one..

	a = 0
	for x in files:
		a = a+1
		print("%s: %s" % (a, x))

#Now it's time to ask about wich preset to choose and activate
#To be sure that a number from the given list have been choosed a while loop with some crazy if.elif.else statements will be used.
#Eg. a test about if it is a number at all, if the number is a part of the list and then to store the preset and send it to the activation module

#The number of entries in the list will be needed too
	filesLen = len(files)
#Well. It's the length, but it's gotta do.

#The choosen preset sets a variable so it can be used in a loop

	choosedFile = int(raw_input("\nPlease choose a preset from the list above by writing the number. "))

	choosePreLoop = True
	while choosePreLoop:

		if 1 <= choosedFile <= filesLen:

#If the input matches one of the listed presets, the file will be read and a var will be stored

			presetName = files[choosedFile-1]
			surePresetName = raw_input("\nYou have choosed %s, is that correct? y/n " % (presetName))

			if surePresetName == "y":

				setupToActivate = open("%s/%s" % (presetDir, presetName), "r").read()
				choosePreLoop = False

			elif surePresetName == "n":

				choosedFile = int(raw_input("\nThen please choose the correct preset. "))
				choosePreLoop = True

			else:

				surePresetName = raw_input("\Please type 'y' or 'n' to activate the preset: %s. " % (presetName))

		else:

			choosedFile = int(raw_input("\nPlease choose a number between 1 and %s. " % (filesLen)))
			choosePreLoop = True

	print("\nYou have choosed preset: %s, with the settings:\n\n%s" % (choosedFile, setupToActivate))


"""
Make a new Setup
"""


def newSetup():

#Is the user chooses to make a new setup we start with the input part.
	newSetupInput = raw_input("Do you want to set up a interface for inpiut? y/n ")

	newSetupInputLoop = True

	while newSetupInputLoop

		if newSetupInput == y:

			inputInterface = subprocess.check_output("alsacap -R", shell=True)

		elif newSetupInput == n:

			newSetupInputLoop = False

		else:

			newSetupInput = raw_input("Please type 'y' or 'n'. ")
			newSetupInputLoop = True



"""
Save the Setup as preset?
"""


"""
Activate Setup
"""

#Next the function begins
def actSetup(x, y):

	global log

	homeDir = x
	GAIADir = y
	actSetupLoop = True
	while actSetupLoop:

		actSetup = raw_input("Do you want to run the setup now? y/n ")

#If answered y, open file (preset), print content, run as command.
#If n, tell where the preset is saved, and quits.

		if actSetup == "y":

			setupToActivateSplitted = setupToActivate.splitlines(True)

			a2jAct = setupToActivateSplitted[0]
			j2aAct = setupToActivateSplitted[1]
			
			rightNow = time.strftime("%d:%m:%Y-%H:%M:%S")

			print "Output from\n\n%s\nwill be saved as GAIA.log in %s.\n" % (setupToActivate, GAIADir)
	
			log = open("GAIA.log", "w")

			subprocess.Popen("%s" % (a2jAct), shell=True, stdout=log).stdout

			time.sleep(1)

			subprocess.Popen("%s" % (j2aAct), shell=True, stdout=log).stdout

			lastChanceLoop = False

		elif actSetup == "n":

			print("Well, see you another time.")

			lastChanceLoop = False

		else:

			print "Please answer with 'y' or 'n'."

			lastChanceLoop = True

		actSetupLoop = False


"""
ZitaStop
"""

#This is the function that will be loaded last. It is simple a function to kill zita again, with a simple safety in.
def stopZita():

	quitZitaLoop = True
	while quitZitaLoop:

#The first operator
		quitZita = raw_input("Press 'q' followed by 'Enter' if/when you want to stop Zita-ajbridge. ")

		print("")

		if quitZita == "q":

#The safety is made by the usual while loop
			sureQuitZitaLoop = True
			while sureQuitZitaLoop:

#The user is asked if he/she is sure
				sureQuitZita = raw_input("Are you sure you want to quit Zita-ajbridge? y/n ")

				if sureQuitZita == "y":

					print("")

#The killall zita-a2j and killall zita-j2a commands will be executed
					subprocess.Popen("killall zita-j2a", shell=True, stdout=log)
					time.sleep(1)
					subprocess.Popen("killall zita-a2j", shell=True, stdout=log)
					sureQuitZitaLoop = False
					quitZitaLoop = False

				elif sureQuitZita == "n":

					sureQuitZitaLoop = False
					quitZitaLoop = True

				else:

					print("Please type in 'y' or 'n'. ")
					sureQuitZitaLoop = True

		else:

			quitZitaLoop = True


	log.close()

	time.sleep(2)

	print("")

	print("Thank you for using nonGAIA!\n")
