#!/usr/bin/python

#Function to run zita-a2j

def runInputPreset():

	presetRunLoop = True
	while presetRunLoop:

		presetRun = raw_input("Activate preset now? y/n ")

#If answered y, open file (preset), print content, run as command.
#If n, tell where the preset is saved, and quits.

		if presetRun == "y":
			preset = open("%s" % (presetName), "r")
			commandToRun = preset.read()

			lastChanceLoop = True
			while lastChanceLoop:
				lastChance = raw_input("This will run '%s', okay? y/n" % (commandToRun))
				if lastChance == "y":

					rightNow = time.strftime("%d:%m:%Y-%H:%M:%S")
					logInput = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE).stdout.read()
					currentDir = os.path.dirname(os.path.abspath(__file__))

					print "Output from %s will be saved in GAIA.log in %s." % (commandToRun, currentDir)
	
					log = open("GAIA.log", "w")
						
					subprocess.Popen("%s" % (commandToRun), shell=True, stdout=log).stdout
	
					log.close()

					lastChanceLoop = False

				elif lastChance == "n":

					raw_input("Well. The preset is saved for later.")

					lastChanceLoop = False

				else:

					print "Please answer with 'y' or 'n'."

					lastChanceLoop = True

			presetRunLoop = False

		elif presetRun == "n":
			

			presetRunLoop = False

		else:
			print "Please type 'y' or 'n'."

			presetRunLoop = True

	presetSaveLoop = False

