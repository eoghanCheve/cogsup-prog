from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_DOWN, K_UP, K_LEFT, K_RIGHT
# from ...package.helper_exp_app import * #doesn't work

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

def make_cross(s, pos=(0,0)):
    c = stimuli.FixCross(size=(15*s, 15*s), line_width=s, position=pos)
    c.preload()
    return c

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
def run_trial(side = 1):
    fixation = make_cross(10, pos=[300*side, 0])

    radius = 75
    circle = make_circle(radius)

    timed_draw([fixation, circle])
    while True :
        key, tr = exp.keyboard.wait(keys = [K_DOWN, K_UP, K_LEFT, K_RIGHT, ord(' ')])
        if key == K_LEFT:
            circle.move(offset = (-10,0))
        if key == K_RIGHT:
            circle.move(offset = (10,0))
        if key == K_UP:
            radius += 10
            circle = make_circle(radius, pos = circle.position)
        if key == K_DOWN and radius > 5:
            radius -= 10
            circle = make_circle(radius, pos = circle.position)
        if key == ord(' ') :
            break
        timed_draw([fixation, circle])


control.start(subject_id=1)

text = stimuli.TextScreen(heading="Finding the blind spot", text="You can use the L and R arrows to move the circle ans Up & Down arrowd to change its size. Begin by closing your left eye and then press a key. If you want to quit, press space.")
text.present()
exp.keyboard.wait()

run_trial()
    
control.end()