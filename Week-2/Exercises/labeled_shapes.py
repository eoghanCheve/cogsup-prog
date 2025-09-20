# Import the main modules of expyriment
from expyriment import design, control, stimuli
import math as m
import random as r


control.set_develop_mode()


# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Labeled Shapes")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

# height = m.sqrt(50**2 - 25**2)/1.5 #distance from edges to center in order to have a triangle of side length af 50
height = 50

triangle = stimuli.Shape(vertex_list=[(height,0), (m.cos((2/3)*m.pi)*height, m.sin((2/3)*m.pi)*height), (m.cos((4/3)*m.pi)*height, m.sin((4/3)*m.pi)*height)], 
                        colour = "purple", position=(-100,0))

# gsquare = stimuli.Shape(vertex_list=[(0,height), (m.sin((2/3)*m.pi)*height, m.cos((2/3)*m.pi)*height), (m.sin((4/3)*m.pi)*height, m.cos((4/3)*m.pi)*height)], 
#                         colour = "purple", position=(-100,0))

hexagon = stimuli.Shape(vertex_list=[(m.cos((i/3)*m.pi)*height/2, m.sin((i/3)*m.pi)*height/2) for i in range(6)], 
                        colour = "yellow", position=(100,0))

lline = stimuli.Line(start_point=(-100,height/2), end_point=(-100,height/2+50), line_width=3)
rline = stimuli.Line(start_point=(100,height/2), end_point=(100,height/2+50), line_width=3)

ltext = stimuli.TextLine(text="triangle", position=(-100,height/2+70))
rtext = stimuli.TextLine(text="Hexagon", position=(100,height/2+70))

#-----------
def render(elements): # a function that render the stimuli in `elements` in the order of the list.
    n = len(elements)
    if n == 1:
        elements[0].present(clear=True, update=True)
    else:
        elements[0].present(clear=True, update=False)
        for i in range(1,n-1):
            elements[i].present(clear=False, update=False)
        elements[-1].present(clear=False, update=True)
#--------------


# Start running the experiment
control.start(subject_id=1)

render([triangle, hexagon, lline, rline, ltext, rtext])



# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()