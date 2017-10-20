#----------Python Spinner----------#
#      Made by _creepersbane       #
# Made for use in conjunction with #
#     the "spin_mod.py" file       #
# To use this module please import #
#        spin_mod instead          #
#----------------------------------#
from time import sleep
import threading
########################################################
# Variables defined here
spinnerFrames = ["\u005F","\u23B8","\u203E","\u23B9"]
stopcheck = False
text = "Dummy Text. Please replace."
########################################################
# This __init__ does nothing :P
def __init__(self):
	return self
# The following functions are for use within the thread
def stopCheck():
	return stopcheck
def getFrames():
	return spinnerFrames
def setFrames(frames):
	spinnerFrames = frames
def stop(): # This is broken
	stopcheck = True
def getText():
	return text
def setText(newText):
	text = newText
# The actual spinner
def spinner():
	text = getText()
	spinnerFrames = getFrames()
	frame = 1
	while not stopCheck():
		print("\r \u001b[2K" + spinnerFrames[(frame - 1) % len(spinnerFrames)] + " " + text,end="",flush=True)
		frame = frame + 1
		sleep(0.1)
def start():
	spinObj = threading.Thread(target=spinner)
	spinObj.start()
def demo():
	try:
		start()
	except KeyboardInterrupt:
		print("")
if __name__ == "__main__":
	demo()
