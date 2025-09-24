from expyriment import design, control, stimuli, misc



_white = misc.constants.C_WHITE



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

def hermann(size = 40, rows = 5, column = 6, space = 10, square_color = "black", background_colour = _white):
    width, height = exp.screen.size
    list_obj = []
    list_obj.append(stimuli.Rectangle(size = (width, height), colour=background_colour)) # If I want to change the background color without reinitializating the exp I guess ?
    
    square_width = (size+space)*column
    square_height = (size+space)*rows
    list_obj.append(stimuli.Rectangle(size = (square_width, square_height), colour=square_color) )
    
    for i in range(column+1):
        x = (square_width/column) * i - (square_width/2)
        list_obj.append(stimuli.Line(start_point=(x, square_height/2 + 1), end_point=(x, -square_height/2 -1), colour=background_colour, line_width=space))
    for i in range(rows+1):
        y = (square_height/rows) * i - (square_height/2)
        list_obj.append(stimuli.Line(start_point=(square_width/2 + 1, y), end_point=(-square_width/2 -1, y), colour=background_colour, line_width=space))
    
    
    render(list_obj)

#---------------main
        

control.set_develop_mode()

# Create an object of class Experiment: This stores the global settings of your experiment & handles the data file, screen, and input devices
exp = design.Experiment(name = "Edge", background_colour=_white)

# Initialize the experiment: Must be done before presenting any stimulus
control.initialize(exp)


# Start running the experiment
control.start(subject_id=1)

hermann(size = 40, rows = 5, column = 6, space = 10)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()