from expyriment import design, control, stimuli


def render(elements): # a function that render the stimuli in `elements` in the order of the list.
    n = len(elements)
    if n == 1:
        elements[0].present(clear=True, update=True)
    else:
        elements[0].present(clear=True, update=False)
        for i in range(1,n-1):
            elements[i].present(clear=False, update=False)
        elements[-1].present(clear=False, update=True)


control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Edge")

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)

width, height = exp.screen.size
swidth = 0.05 * width
long = width/2 - swidth/2
lat = height/2 - swidth/2

square_list = [stimuli.Rectangle(line_width=1, size=(swidth,swidth), colour="red", 
                                 position=((i%2)*long*2 - long, (j%2)*lat*2 - lat)) for i in range(2) for j in range(2)]
#I initializated every square in one line because I can.

# Start running the experiment
control.start(subject_id=1)

render(square_list)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()