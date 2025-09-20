# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()


# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Square")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

gsquare = stimuli.Rectangle(size=(50,50), colour="green", position=(100,0))

rsquare = stimuli.Rectangle(size=(50,50), colour="red", position=(-100,0))

# Start running the experiment
control.start(subject_id=1)

gsquare.present(clear=True, update=False)
# Present the fixation cross
rsquare.present(clear=False, update=True)



# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()