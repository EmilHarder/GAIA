#!/usr/bin/python

import subprocess
import time
import os
"""
list1 = ['A', 'Komplete Audio 6', 'Komplete Audio 6 og iConnectMIDI4', 'Preset1', 'Preset2', 'asdf\xc3\xa6lkj adslfkjh asldfkjh']
list1Len = len(list1)

#print(list1[2])

y = 0

while y < list1Len:
	y = y+1
	print(list1)
"""

liste = ['A', 'Komplete Audio 6', 'Komplete Audio 6 og iConnectMIDI4', 'Preset1', 'Preset2', 'asdf\xc3\xa6lkj adslfkjh asldfkjh']
listLen = len(liste)
#for list in list_of_lists:
a = 0
for x in liste:
	a = a+1
	print("%s: %s" % (a, x))
