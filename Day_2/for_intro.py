from psychopy import visual, core, event

win = visual.Window((800,800))

visual.TextStim(win, "Hello World!").draw()

win.flip()

core.wait(1)

visual.ImageStim(win, "cat.png").draw()

win.flip()

event.waitKeys()