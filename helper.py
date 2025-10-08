from expyriment import design, control, stimuli

def timed_draw(exp, stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    elapsed = exp.clock.time - t0
    return elapsed


def present_for(exp, stims, time):
    if time == 0:
        return
    dt = timed_draw(stims)
    if dt > 0:
        exp.clock.wait(time - dt)
