# Import the main modules of expyriment
from expyriment import design, control, stimuli

control.set_develop_mode()

def render(elements): # a function that render the stimuli in `elements` in the order of the list.
    n = len(elements)
    if n == 1:
        elements[0].present(clear=True, update=True)
    else:
        elements[0].present(clear=True, update=False)
        for i in range(1,n-1):
            elements[i].present(clear=False, update=False)
        elements[-1].present(clear=False, update=True)
        
#-----------

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Launching Disrupt Space")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

gsquare = stimuli.Rectangle(size=(50,50), colour="green", position=(0,0))

rsquare = stimuli.Rectangle(size=(50,50), colour="red", position=(-400,0))

condition = True

#-----------------

# Start running the experiment
control.start(subject_id=1)
exp.clock.reset_stopwatch() # I use this to mark the begining time of the experiment

render([rsquare ,gsquare])
while condition:
    time = exp.clock.stopwatch_time
    #-----Modifications on each objects
    if rsquare.absolute_position[0] <= -20:
        rsquare.move(offset=(4,0))
        exp.clock.reset_stopwatch()
    else:
        gsquare.move(offset=(4,0))
    
    #-----Condition update-----
    condition = gsquare.absolute_position[0] <= 400 #The condition is for the green square to be on the left side of (400,0)
    #----Rendering------
    # exp.clock.wait(1)
    render([rsquare ,gsquare]) # at each frame, we reders the elements

    


# End the current session and quit expyriment
control.end()