from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT
# from ...package.helper_exp_app import * #doesn't work

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(["block nb", "trial nb", "type", "word", "color", "RT", "accuracy"])
control.set_develop_mode()
control.initialize(exp)

colors = ["red", "blue", "green", "orange"]

""" Stimuli """

"""helper"""
def timed_draw(stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    elapsed = exp.clock.time - t0
    return elapsed


def present_for(stims, time):
    if time == 0:
        return
    dt = timed_draw(stims)
    if dt > 0:
        exp.clock.wait(time - dt)


""" Experiment """
def run_trial(same_color):
    ind = design.randomize.rand_int(0,4)
    text_display = colors[ind]
    if same_color :
        color_display = text_display
    else :
        color_display = design.randomize.rand_element(colors[0:ind]+colors[ind+1:-1])
    text = stimuli.TextLine(text=text_display, text_colour=color_display)
    key, tr = exp.keyboard.wait(keys = [ord("y"), ord("Y"), ord("n"), ord("N"), ord(' ')])

    timed_draw([])

def run_block():
    text = stimuli.TextScreen(heading="Finding the stroop dog", text="Type \"Y\" if it is the same color as the text, \"N\" else.\nPress space to finnish")
    text.present()
    exp.keyboard.wait()
    block+=1

control.start(subject_id=1)

exp.keyboard.wait()

block = 1
run_block()
    
control.end()