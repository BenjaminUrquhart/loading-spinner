# loading-spinner

An incredibly simple "loading spinner" for python projects

# Installing

`pip install loadingspinner`

# Usage

NOTE: Please do NOT import spinner. You MUST use loadingspinner.

`import loadingspinner
loadingspinner.setText("Loading...")
loadingspinner.setTextColor("yellow")
loadingspinner.start()
<lines of code>
loadingspinner.stop()`

# Customizing the spinner

Changing the spinner animation:

`loadingspinner.setFrames(<list of characters to display in order from left to right>)`

Ex. `loadingspinner.setFrames(["|","/","-","\\"])`

Changing the text color:
`
loadingspinner.setTextColor(<any valid Colorama color>)`

Ex. `loadingspinner.setTextColor("red")`

Changing the spinner color:

NOTE: This feature is not fully implemented and any changes to the spinner color will change the text color as well

`loadingspinner.setSpinnerColor(<any valid Colorama color>)`

Ex. `loadingspinner.setSpinnerColor("yellow")`
