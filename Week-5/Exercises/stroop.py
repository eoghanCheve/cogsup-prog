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
def run_trial(same_color, block_nb, trial_nb):
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
    acc = 0
    if ((key == ord("y") or key == ord("Y")) and same_color) or ((key == ord("n") or key == ord("N")) and not same_color):
        acc = 1
    exp.data.add([block_nb, trial_nb, type, text_display, color_display, tr, acc])
    if key == ord(' ') :
        return 1
    else :
        return 0


def run_block(block_nb):
    text = stimuli.TextScreen(heading="Finding the stroop", text="Type \"Y\" if it is the same color as the text, \"N\" else.\nPress space to finnish")
    text.present()
    exp.keyboard.wait()
    for i in range(10):
        cond = design.randomize.rand_int(0,1)
        if run_trial(cond, block_nb, i) :
            return 0
    return 1

control.start(subject_id=1)

exp.keyboard.wait()

if run_block(1) :
    run_block(2)
    
control.end()