# Import the main modules of expyriment
from expyriment import design, control, stimuli
import math as m
import random as r

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Launching Random Motion")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

rsquare = stimuli.Rectangle(size=(50,50), colour="red", position=(-400,0))

gsquare = stimuli.Rectangle(size=(50,50), colour="green", position=(0,0))

condition = True

#------------------------

def render(elements): # a function that render the stimuli in `elements` in the order of the list.
    n = len(elements)
    if n == 1:
        elements[0].present(clear=True, update=True)
    else:
        elements[0].present(clear=True, update=False)
        for i in range(1,n-1):
            elements[i].present(clear=False, update=False)
        elements[-1].present(clear=False, update=True)

def launching_function(tgap = 0, sgap = 0, speeddiff = 0):
    theta = r.random()*m.pi*2
    dirvector = (m.cos(theta), m.sin(theta))
    speedvector = (-dirvector[0]*5,-dirvector[1]*5)
    posvector = (dirvector[0]*300,dirvector[1]*300)
    print(dirvector)
    rsquare = stimuli.Rectangle(size=(50,50), colour="red", position=posvector)
    gsquare = stimuli.Rectangle(size=(50,50), colour="green", position=(0,0))


    condition = True
    flag = True

    while condition:
        time = exp.clock.stopwatch_time
        #-----Modifications on each objects
        if not rsquare.overlapping_with_stimulus(gsquare)[0] and flag :
            rsquare.move(offset=speedvector)
            exp.clock.reset_stopwatch()
        elif time >= tgap:
            flag = False
            gsquare.move(offset=speedvector)

        #-----Condition update-----
        condition = m.sqrt(gsquare.absolute_position[0]**2 + gsquare.absolute_position[1]**2) <= 300 #The condition is for the green square to be farther than 300 px
        #----Rendering------
        # exp.clock.wait(1)
        render([rsquare ,gsquare]) # at each frame, we reders the elements
        
#-----------


# Start running the experiment
control.start(subject_id=1)
exp.clock.reset_stopwatch() # I use this to mark the begining time of the experiment
launching_function()
launching_function()
launching_function()


    


# End the current session and quit expyriment
control.end()