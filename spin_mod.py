import spinner
def setText(text):
	spinner.text = text
def setFrames(frames):
	spinner.spinnerFrames = frames
def start():
	spinner.stopcheck = False
	spinner.start()
def stop():
	spinner.stopcheck = True
