# Import the main modules of expyriment
from expyriment import design, control, stimuli
import math as m
import random as r


control.set_develop_mode()



# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Labeled Shapes")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

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

def generate_poly(nb_vertex, height = 50, position = (0,0), colour = "blue"):
    return stimuli.Shape(vertex_list=[(m.cos((i/nb_vertex)*m.pi*2)*height, m.sin((i/nb_vertex)*m.pi*2)*height) for i in range(nb_vertex)], 
                        colour = colour, position=position)

#--------------

height = 50

triangle = generate_poly(3, position=(-100,0), colour="purple")

# gsquare = stimuli.Shape(vertex_list=[(0,height), (m.sin((2/3)*m.pi)*height, m.cos((2/3)*m.pi)*height), (m.sin((4/3)*m.pi)*height, m.cos((4/3)*m.pi)*height)], 
#                         colour = "purple", position=(-100,0))

hexagon = generate_poly(10, position=(100,0), colour="yellow")

lline = stimuli.Line(start_point=(-100,height/2), end_point=(-100,height/2+50), line_width=3)
rline = stimuli.Line(start_point=(100,height/2), end_point=(100,height/2+50), line_width=3)

ltext = stimuli.TextLine(text="triangle", position=(-100,height/2+70))
rtext = stimuli.TextLine(text="Hexagon", position=(100,height/2+70))




# Start running the experiment
control.start(subject_id=1)

render([triangle, hexagon, lline, rline, ltext, rtext])



# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()