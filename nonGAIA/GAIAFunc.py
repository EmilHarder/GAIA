#!/usr/bin/python3

#First there is the importing of external modules:
import subprocess
import time
import os

"""
First of is the function to choose a preset and run it.
"""

def choosePre(homeDir):

#Then make a list of the stored files (presets) in the preset folder in .GAIA

#First a var has to be set for the preset directory
	presetDir = "%s/.GAIA/Presets" % (homeDir)

#And the files in the directory has to get sorted
	files = sorted(os.listdir("%s/.GAIA/Presets" % (homeDir)))

#Soted list of presets can be shown with numbers in front, tada!
#Didn't think I would survive that one..

	a = 0
	for n in files:
		a = a+1
		print("%s: %s" % (a, n))


	"""
	Now it's time to ask about wich preset to choose and activate
	To be sure that a number from the given list have been choosed
	a while loop with some crazy if.elif.else statements will be used.
	Eg. a test about if it is a number at all, if the number is a part
	of the list and then to store the preset and send it to the
	activation module
	"""

#The number of entries in the list will be needed too
	filesLen = len(files)
#Well. It's the length, but it's gotta do.

	emptyDirCheck = True
	while emptyDirCheck:

		if filesLen == 0:

			returnToStart = input("There is no presets stored. Return to start? y/n")

			if returnToStart == "y" or returnToStart == "Y":

				break
				emptyDirCheck == False

			else:

				print("Well what then?")

		else:

#The choosen preset sets a variable so it can be used in a loop

			choosedFile = input("\nPlease choose a preset from the list above by writing the number. ")

			choosedFileLoop = True
			while choosedFileLoop:

				try: 
					choosedFileInt = int(choosedFile)
					choosedFileLoop = False
				except ValueError:
					choosedFile = input('\nPlease write a number. E.g. \'1\' or \'4\'')
					choosedFileLoop = True

			choosePreLoop = True
			while choosePreLoop:

				if 1 <= choosedFileInt <= filesLen:

#If the input matches one of the listed presets, the file will be read and a var will be stored

					presetName = files[choosedFileInt-1]
					surePresetName = input("\nYou have choosed %s, is that correct? y/n " % (presetName))

					if surePresetName == "y":

						setupToActivate = open("%s/%s" % (presetDir, presetName), "r").read()
						choosePreLoop = False

					elif surePresetName == "n":

						choosedFile = input("\nThen please choose the correct preset. ")

						try: 
							choosedFileInt = int(choosedFile)
						except ValueError:
							choosedFile = input('\nPlease write a number. E.g. \'1\' or \'4\'')

						choosePreLoop = True

					else:

						surePresetName = input("\Please type 'y' or 'n' to activate the preset: %s. " % (presetName))

				else:

					choosedFileInt = int(input("\nPlease choose a number between 1 and %s. " % (filesLen)))
					choosePreLoop = True

			print("\nYou have choosed preset: %s, with the settings:\n\n%s" % (choosedFile, setupToActivate))

			break
		

"""
WORK IN PROGRESS IN TEST.PY§!
"""

	
"""
Activate Setup
"""

#Next the function begins
def actSetup(x, y):

	homeDir = x
	GAIADir = y
	actSetupLoop = True
	while actSetupLoop:

		actSetup = input("Do you want to run the setup now? y/n ")

#If answered y, open file (preset), print content, run as command.
#If n, tell where the preset is saved, and quits.

		if actSetup == "y":

			log = open("GAIA.log", "w")

			setupToActivateSplitted = setupToActivate.splitlines(True)

			a2jAct = setupToActivateSplitted[0]
			j2aAct = setupToActivateSplitted[1]

			print ("Output from\n\n%s\nwill be saved as GAIA.log in %s." % (setupToActivate, GAIADir))

			subprocess.Popen("%s" % (a2jAct), shell=True, stdout=log).stdout

			time.sleep(1)

			subprocess.Popen("%s" % (j2aAct), shell=True, stdout=log).stdout

			lastChanceLoop = False

			log.close()

		elif actSetup == "n":

			print("Well, see you another time.")

			lastChanceLoop = False

		else:

			print ("Please answer with 'y' or 'n'.")

			lastChanceLoop = True

		actSetupLoop = False


"""
ZitaStop
"""

#This is the function that will be loaded last. It is simple a function to kill zita again, with a simple safety in.
def stopZita():

	log = open("GAIA.log", "w")

	quitZitaLoop = True
	while quitZitaLoop:

#The first operator
		quitZita = input("Press 'q' followed by 'Enter' if/when you want to stop Zita-ajbridge. ")

		print("")

		if quitZita == "q":

#The safety is made by the usual while loop
			sureQuitZitaLoop = True
			while sureQuitZitaLoop:

#The user is asked if he/she is sure
				sureQuitZita = input("Are you sure you want to quit Zita-ajbridge? y/n ")

				if sureQuitZita == "y":

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
