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
exp = design.Experiment(name = "Triggering")

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
    #-----Modifications on each objects
    if rsquare.absolute_position[0] <= -50:
        rsquare.move(offset=(2,0))
    else:
        gsquare.move(offset=(6,0))
    
    #-----Condition update-----
    time = exp.clock.stopwatch_time
    condition = time < 1000 #The condition is for the experiment to last less than 1 sec
    #----Rendering------
    # exp.clock.wait(1)
    render([rsquare ,gsquare]) # at each frame, we reders the elements

    


# End the current session and quit expyriment
control.end()