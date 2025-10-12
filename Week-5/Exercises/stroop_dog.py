from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT
# from ...package.helper_exp_app import * #doesn't work

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(["block nb", "trial nb", "type", "word", "color", "RT", "accuracy"])
control.set_develop_mode()
control.initialize(exp)

colors = ["red", "blue", "green", "orange"]
block = 1
trial = 1

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
    type = "mismatch"
    ind = design.randomize.rand_int(0,3)
    text_display = colors[ind]
    if same_color :
        type = "match"
        color_display = text_display
    else :
        color_display = design.randomize.rand_element(colors[0:ind]+colors[ind+1:4])
    text = stimuli.TextLine(text=text_display, text_colour=color_display)
    timed_draw([text])
    key, tr = exp.keyboard.wait(keys = [ord("y"), ord("Y"), ord("n"), ord("N"), ord(' ')])
    exp.data.add([block, trial, type, text_display, color_display, tr, "todo"])


def run_block():
    text = stimuli.TextScreen(heading="Finding the stroop", text="Type \"Y\" if it is the same color as the text, \"N\" else.\nPress space to finnish")
    text.present()
    exp.keyboard.wait()
    trial = 1
    for _ in range(10):
        trial += 1
        cond = design.randomize.rand_int(0,1)
        run_trial(cond)
    block+=1

control.start(subject_id=1)

exp.keyboard.wait()

block = 1
run_block()
run_block()
    
control.end()