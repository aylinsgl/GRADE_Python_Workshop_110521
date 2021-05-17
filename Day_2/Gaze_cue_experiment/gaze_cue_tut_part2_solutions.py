#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
GRADE brain workshop, Ma 11-12th 2021
Authors: Aylin Kallmayer, Melvin Kallmayer, Leah Kumle

Gaze Cue Experiment
Trial sequence: Fixation cross (750ms) - neutral gaze (750ms) - cue (500ms) - Target and distractor - response
Logs variables and responses in output file "yourname.csv"
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

# assign subject id
subject_id = "yourname"

# create a window to draw in
win = visual.Window((800, 600), fullscr=False, units='pix', pos=(0,0))

# Global event key to quit the experiment ("shutdown key").
event.globalKeys.add(key='q', func=core.quit)

# prepare output file
filename = subject_id + ".csv"
file = open(filename, "w", encoding='utf8')
writer = csv.writer(file, delimiter = ",")

# write the column names of the variables we want to log
writer.writerow(["subject_id","gaze","target","position","response","accuracy"])

#-----------------------------------------------------#
#----DEFINE CONDITIONS
#-----------------------------------------------------#

# Here we store our conditions for the trials: 
conditions = [("left", "F", "left"),
                        ("right", "F", "left"),
                        ("left","F","right"),
                        ("right","F","right"),
                        ("left","H","left"),
                        ("right","H","left"),
                        ("left","H","right"),
                        ("right","H","right")
                        ]

#-----------------------------------------------------#
#----DEFINE FUNCTIONS
#-----------------------------------------------------#

def one_trial(gaze, target, target_pos):
    '''create one trial sequence given gaze, target letter and target position ("left" or "right").'''
    # 1) first, present fixation cross
    # put your code here
    present_fix_cross()
    
    # 2) present neutral gaze image
    present_neutral_gaze()
    
    # 3) present gaze cue
    present_gaze_cue(gaze)
    
    # 4.1) present response screen
    response = make_response_screen(gaze, target, target_pos)
    return response

def present_fix_cross():
    '''Present a fixation cross (+) in the middle of the screen for 750ms.'''
    # put your code here
    visual.TextStim(win, "+", pos=(0,0)).draw()
    win.flip()
    core.wait(0.75)
    
def present_neutral_gaze():
    '''Present the "gaze_neutral.png" image in the center of the screen for 750ms.'''
    visual.ImageStim(win, "stimuli/gaze_neutral.png", pos=(0,0)).draw()
    win.flip()
    core.wait(0.75)

def present_gaze_cue(gaze):
    '''Present the gaze cue image in the center of the screen for 500ms. Gaze can be either left or right'''
    path = "stimuli/gaze_" + gaze + ".png"
    visual.ImageStim(win, path, pos=(0,0)).draw()
    win.flip()
    core.wait(0.5)

def make_response_screen(gaze, target, target_pos):
    '''Create window presenting gaze cue, target and distractor letter'''
    if target_pos == "left":
        target_tuple = (-200,0)
        dist_tuple = (200,0)
    elif target_pos == "right":
        target_tuple = (200,0)
        dist_tuple = (-200,0)
    path = "stimuli/gaze_" + gaze + ".png"
    visual.ImageStim(win, path, pos=(0,0)).draw()
    visual.TextStim(win, text=target, pos=target_tuple).draw()
    visual.TextStim(win, text="X", pos=dist_tuple).draw()
    win.flip()
    response = event.waitKeys(keyList=["y","m"])[0]
    return response
    
def end_screen():
    visual.TextStim(win, "END", pos=(0,0)).draw()
    win.flip()
    core.wait(1)

def get_correct_response(target):
    '''Get correct response key based on target letter'''
    if target == "F":
        correct_response = "y"
    else:
        correct_response = "m"
    return correct_response

#-----------------------------------------------------#
#----RUN EXPERIMENT
#-----------------------------------------------------#
# randomize items of list
shuffle(conditions)

# run multiple trials
for trial in conditions:
    gaze, target, target_pos = trial
    response = one_trial(gaze,target,target_pos)
    corr_response = get_correct_response(target)
    if response == corr_response:
        accuracy=1
    else:
        accuracy=0
    writer.writerow([subject_id, gaze, target, target_pos, response, accuracy])

end_screen()

