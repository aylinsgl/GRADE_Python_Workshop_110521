#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GRADE brain workshop, Ma 11-12th 2021
Authors: Aylin Kallmayer, Melvin Kallmayer, Leah Kumle

Gaze Cue Experiment
Trial sequence: Fixation cross (750ms) - neutral gaze (750ms) - gaze cue left (500ms) - Target F left and distractor X right - keypress response
"""

#-----------------------------------------------------#
#----SET UP
#-----------------------------------------------------#

# import libraries
from __future__ import division
from __future__ import print_function

from psychopy import visual, event, core, logging, sound, monitors, data
from random import shuffle
import numpy as np
import csv

# create a window
win = visual.Window((800, 600), fullscr=False, units='pix', pos=(0,0))

# Global event key "q" to quit the experiment ("shutdown key").
event.globalKeys.add(key='q', func=core.quit)

#-----------------------------------------------------#
#----DEFINE CONDITIONS
#-----------------------------------------------------#

# Here we store our conditions for the trial: gaze (left), target letter (F), and target position (left)
conditions = ["left", "F", "left"]

#-----------------------------------------------------#
#----DEFINE FUNCTIONS
#-----------------------------------------------------#

def one_trial(gaze, target, target_pos):
    '''create one trial sequence given gaze, target letter and target position ("left" or "right").'''
    # 1) first, present fixation cross
    # call function to present fixation cross here after you've defined it
    present_fix_cross()

    # 2) present neutral gaze image
    # call function to present neutral gaze image here after you've defined it
    present_neutral_gaze()

    # 3) present gaze cue
    # call function to present left gaze image here after you've defined it
    present_gaze_cue(gaze)

    # 4) present response screen
    # call function to present response screen here after you've defined it
    make_response_screen(gaze, target, target_pos)

    # End screen
    end_screen()

#----1)
def present_fix_cross():
    '''Present a fixation cross (+) in the middle of the screen for 750ms.'''
    # put your code here
    visual.TextStim(win, "+", pos=(0,0)).draw()
    win.flip()
    core.wait(0.75)

#----2)
def present_neutral_gaze():
    '''Present the "gaze_neutral.png" image in the center of the screen for 750ms.'''
    # put your code here
    visual.ImageStim(win, "stimuli/gaze_neutral.png", pos=(0,0)).draw()
    win.flip()
    core.wait(0.75)

#----3)
def present_gaze_cue(gaze):
    '''Present the gaze cue image in the center of the screen for 500ms. Gaze can be either left or right'''
    # put your code here
    path = "stimuli/gaze_"+gaze+".png"
    visual.ImageStim(win, path, pos=(0,0)).draw()
    win.flip()
    core.wait(0.5)

#----4)
def make_response_screen(gaze, target, target_pos):
    '''Create window presenting gaze cue, target and distractor letter'''
    # put your code here
    target_tuple = (-200,0)
    dist_tuple = (200,0)
    path = "stimuli/gaze_"+gaze+".png"
    visual.ImageStim(win, path, pos=(0,0)).draw()
    visual.TextStim(win, target, pos=target_tuple).draw()
    visual.TextStim(win, "X", pos=dist_tuple).draw()
    win.flip()
    event.waitKeys(keyList=["y","m"])

def end_screen():
    visual.TextStim(win, "END", pos=(0,0)).draw()
    win.flip()
    core.wait(1)

#-----------------------------------------------------#
#----RUN EXPERIMENT
#-----------------------------------------------------#

gaze, target, target_pos = conditions


#### run single trial
one_trial(gaze, target, target_pos)

##### run multiple trials
