from expyriment import design, control, stimuli, misc

grey = misc.constants.C_GREY



#---------------functions

def render(elements): # a function that render the stimuli in `elements` in the order of the list.
    n = len(elements)
    if n == 1:
        elements[0].present(clear=True, update=True)
    else:
        elements[0].present(clear=True, update=False)
        for i in range(1,n-1):
            elements[i].present(clear=False, update=False)
        elements[-1].present(clear=False, update=True)

def kanisa(scaling_circle = 1, scaling_Rectangle = 1, rectangle_ratio = 1) :
    width, height = exp.screen.size
    swidth = 0.05 * width * scaling_circle
    bheight = 0.25 * width * scaling_Rectangle
    bwidth = bheight * rectangle_ratio
    long = bwidth/2
    lat = bheight/2

    forme_list = [stimuli.Circle(radius=swidth, colour="black" if j else "white", position=((i%2)*long*2 - long, (j%2)*lat*2 - lat)) for i in range(2) for j in range(2)]
    #I did every circle on one line again because I can again !
    forme_list.append(stimuli.Rectangle(size=(bwidth,bheight), colour=grey, position=(0,0)))
    #I didn't have the patience to put the square on the previous line, but it can be done

    render(forme_list)

#---------------main
        

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Edge", background_colour=grey)

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)


# Start running the experiment
control.start(subject_id=1)

kanisa(1, 1.5, 2)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()