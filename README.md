# loading-spinner

An incredibly simple "loading spinner" for python projects

# Usage

NOTE: Please do NOT import spinner. You MUST use spin_mod.

`import spin_mod`

`spin_mod.setText("Loading...")`

`spin_mod.start()`

`<lines of code>`

`spin_mod.stop()`

# Customizing the spinner

Changing the spinner animation:

`spin_mod.setFrames(<list of characters to display in order from left to right>)`

Ex. `spin_mod.setFrames(["|","/","-","\\"])`
