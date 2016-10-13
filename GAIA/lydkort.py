#!/usr/bin/python -B

#This is the first, earliest and simpliest version. (0.000001?)

#The script gives a list of connected audio devices for recording
#based on alsacap.
#Then the user is asked to choose card, device, sample rate etc.
#After that, zita-ajbridge is used to bridge the chosen cards and devices to jack.

#The goal is to make this a simpler and prettier solution by time.
#But first all the mechanics have to work. 
#Remember that alsacap have to be intalled too.

#Importering of used libs

import interfaceSetup
import presetSave
import subprocess
import time
import os

#First the input. (zita-a2j)
#It's a while loop, that use the imported modules inputScript and presetSave

setupInputInterfaceLoop = True
while setupInputInterfaceLoop:

	setupInputInterface = raw_input("Set up a interface for input? y/n ")

	if setupInputInterface == "n":

		print "Well then"
		setupInputInterfaceLoop = False

	elif setupInputInterface == "y":
		
		interfaceSetup.inputInterface()
		setupInputInterfaceLoop = False

		presetSave.presetInput()

#Answer to wether or not to show list of interfaces. This one repeats the list.

	else:
		print "Please enter y or n."

#With the input preset saved it's time to move on to the output.

setupOutputInterfaceLoop = True
while setupOutputInterfaceLoop:

	setupOutputInterface = raw_input("Set up a interface for output? y/n ")

	if setupOutputInterface == "n":

		print "Well then"
		setupOutputInterfaceLoop = False

	elif setupOutputInterface == "y":
		
		interfaceSetup.outputInterface()
		setupOutputInterfaceLoop = False

		presetSave.presetOutput()

#Answer to wether or not to show list of interfaces. This one repeats the list.

	else:
		print "Please enter y or n."

#With the output preset saved it's time to move on to the output.



raw_input("Thank you for using GAIA ('Graphical' Audio Interface Aggregation)!")

#Sleep tight
