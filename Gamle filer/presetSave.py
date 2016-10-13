#!/usr/bin/python

import interfaceSetup
import subprocess
import time
import os

#Function to save the preset for the input interface

def presetInput():

	presetInputSaveLoop = True

	while presetInputSaveLoop:

		presetInputName = raw_input("What do you want to name the preset for the input interface? ")

#A test to be sure that the preset gets a name

		if presetInputName == "":
			print "Please use a name for the preset. Ok?"
			presetInputSaveLoop = True

		else:

			zitaInputInterface = "hw:%s,%s" % (interfaceSetup.choosedInputCard, interfaceSetup.choosedInputDevice)
			presetInput = open("%s.preset" % (presetInputName), "w")
			presetInput.write("zita-a2j -d %s -c %s -r %s"  % (zitaInputInterface, interfaceSetup.choosedInputChannels, interfaceSetup.choosedInputRate))
			presetInput.close()

			currentDir = os.path.dirname(os.path.abspath(__file__))
			print "Preset is saved as '%s.preset' in %s." % (presetInputName, currentDir)

			presetInputSaveLoop = False

#Now the input preset is saved.

#Function to save the preset for the output interface

def presetOutput():

	presetOutputSaveLoop = True

	while presetOutputSaveLoop:

		presetOutputName = raw_input("What do you want to name the preset to the output interface? ")

#A test to be sure that the preset gets a name

		if presetOutputName == "":
			print "Please use a name for the preset. Ok?"
			presetOutputSaveLoop = True

		else:

			zitaOutputInterface = "hw:%s,%s" % (interfaceSetup.choosedOutputCard, interfaceSetup.choosedOutputDevice)
			presetOutput = open("%s.preset" % (presetOutputName), "w")
			presetOutput.write("zita-j2a -d %s -c %s -r %s"  % (zitaOutputInterface, interfaceSetup.choosedOutputChannels, interfaceSetup.choosedOutputRate))
			presetOutput.close()

			currentDir = os.path.dirname(os.path.abspath(__file__))
			print "Preset is saved as '%s.preset' in %s." % (presetOutputName, currentDir)

			presetOutputSaveLoop = False

#Now the output preset is saved.
