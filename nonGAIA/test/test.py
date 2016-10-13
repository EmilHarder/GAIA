#!/usr/bin/python3 -B

import subprocess
import time
import os


"""
Another option is to make a new setup.
The approach is to set up a while loop. Inside that loop set up a if-elif-else for setting up input (zita-a2j) and/or output (zita-j2a). Inside those statements listing the connected interfaces with alsacap and choosing the settings to use. The listning is done by writing the output from alsacap to a text file, and then reading the needed lines from that file.
The devices that are reported 'busy' by alsacap, is skipped. If there are no cards available a message about that will be displayed, and the user can continue. Either with another option about input and output, or to run another function.
Before breaking the loop is the naming of the preset, and returning the preset, for if the user wants to run it.
"""

def newSetup():

	newSetupLoop = True
	while newSetupLoop:

		choosedIO = input("Do you want to set up Zita-bridge for inputs (1), outputs (2) or both (3)? ")

		if choosedIO == "1":

			inputDevices = subprocess.check_output(['alsacap', '-R'])
			inputDevicesDecoded = inputDevices.decode()
			
			alsacapOut = open("alsacapOut", "w")

			alsacapOut.write(inputDevicesDecoded)

			newSetupLoop = False

		elif choosedIO == "2":
		
			inputDevices = subprocess.check_output(['alsacap'])
			inputDevicesDecoded = inputDevices.decode()
			
			alsacapOut = open("alsacapIn", "w")

			alsacapOut.write(inputDevicesDecoded)

			newSetupLoop = False

		elif choosedIO == "3":

			print("Kommer senere")
			newSetupLoop = False

		else:

			print("\nPlease type in the numbers '1', '2' or '3'.\n")
			newSetupLoop = True

newSetup()
