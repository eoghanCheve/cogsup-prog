from expyriment import design, control, stimuli
import random


def load(stims):
    for stim in stims: 
        stim.preload()
def timed_draw(elements):
    n = len(elements)
    if n == 1:
        elements[0].present(clear=True, update=True)
    else:
        elements[0].present(clear=True, update=False)
        for i in range(1,n-1):
            elements[i].present(clear=False, update=False)
        elements[-1].present(clear=False, update=True)
    # return the time it took to draw

def present_for(elements, t=1000):
    n = len(elements)
    t0 = exp.clock.time
    if n == 1:
        elements[0].present(clear=True, update=True)
    else:
        elements[0].present(clear=True, update=False)
        for i in range(1,n-1):
            elements[i].present(clear=False, update=False)
        elements[-1].present(clear=False, update=True)
    t1 = exp.clock.time - t0
    exp.clock.wait(t - t1)

def ternus(ISI = 0, color = False, radius = 50):
    circles = [stimuli.Circle(colour="blue", position=((i*radius*2.5)-3.75
                                                      *radius,0), radius=radius) for i in range(4)]
    load(circles)
    for i in range(10):
        present_for(circles[0:3], 200)
        if ISI > 5 :
            t0 = exp.clock.time
            bscreen.present()
            t1 = exp.clock.time - t0
            exp.clock.wait(ISI - t1)
        present_for(circles[1:4], 200)
        if ISI > 5 :
            t0 = exp.clock.time
            bscreen.present()
            t1 = exp.clock.time - t0
            exp.clock.wait(ISI - t1)

""" Test functions """
exp = design.Experiment()

control.set_develop_mode()
control.initialize(exp)

bscreen = stimuli.BlankScreen()

ternus(0, False)
ternus(50, False)


control.end()
