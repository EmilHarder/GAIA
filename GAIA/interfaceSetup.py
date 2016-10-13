#!/usr/bin/python

import presetSave
import subprocess
import time
import os

#Function to set up interface for the input

def inputInterface():

	chooseInputInterfaceLoop = True

	while chooseInputInterfaceLoop:

		inputInterface = subprocess.check_output("alsacap -R", shell=True)

		print inputInterface

		global choosedInputCard, choosedInputDevice, choosedInputChannels, choosedInputRate

		choosedInputCard = raw_input("Choose card to use. Eg '1'\n")

		choosedInputDevice = raw_input("Choose device to use. Eg '0'\n")

		choosedInputChannels = raw_input("Choose number channels to use. Eg '2'\n")

		choosedInputRate = raw_input("Choose sample rate to use. Eg '44100'\n")

		print "Your settings for zita-a2j will be:\nHw:%s,%s, with %s channel(s) and a sample rate of %s." % (choosedInputCard, choosedInputDevice, choosedInputChannels, choosedInputRate)

#Check result.
		acceptInputCardLoop = True

		while acceptInputCardLoop:

			acceptInput = raw_input("Is that what you want? y/n ")

			if acceptInput == "y":
				acceptInputCardLoop = False
				chooseInputInterfaceLoop = False

			elif accept == "n":
				print "Start over then."
				acceptInputCardLoop = False
				chooseInputInterfaceLoop = True

			else:
				print "Please enter y or n."
				acceptInputCardLoop = True
				chooseInputInterfaceLoop = True

#Input is now set up


#Function to set up interface for the output

def outputInterface():

	chooseOutputInterfaceLoop = True

	while chooseOutputInterfaceLoop:

		outputInterface = subprocess.check_output("alsacap", shell=True)

		print outputInterface

		global choosedOutputCard, choosedOutputDevice, choosedOutputChannels, choosedOutputRate

		choosedOutputCard = raw_input("Choose card to use. Eg '1'\n")

		choosedOutputDevice = raw_input("Choose device to use. Eg '0'\n")

		choosedOutputChannels = raw_input("Choose number channels to use. Eg '2'\n")

		choosedOutputRate = raw_input("Choose sample rate to use. Eg '44100'\n")

		print "Your settings for zita-j2a will be:\nHw:%s,%s, with %s channel(s) and a sample rate of %s." % (choosedOutputCard, choosedOutputDevice, choosedOutputChannels, choosedOutputRate)

#Check result.
		acceptOutputCardLoop = True

		while acceptOutputCardLoop:

			acceptOutput = raw_input("Is that what you want? y/n ")

			if acceptOutput == "y":
				acceptOutputCardLoop = False
				chooseOutputInterfaceLoop = False

			elif accept == "n":
				print "Start over then."
				acceptOutputCardLoop = False
				chooseOutputInterfaceLoop = True

			else:
				print "Please enter y or n."
				acceptOutputCardLoop = True
				chooseOutputInterfaceLoop = True

#Output is now set up

