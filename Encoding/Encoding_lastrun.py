﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on November 17, 2022, at 11:47
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'FacesNamesProffessions_Encoding'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\emilo\\OneDrive - Lund University\\Jobb\\Experiments\\FacesNamesProffessions\\Encoding\\Encoding_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=False, screen=0, 
    winType='glfw', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='white', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Instruktioner:\n\nDu kommer att se bilder på ansikten presenterade en i taget.\nUnder varje bild så står ett NAMN eller ett YRKE .\nDin uppgift är att memorera varje persons namn eller yrke.\n\nDärefter kommer du se de ansikten som du nyss såg men istället för att det står ett namn eller ett yrke under varje bild så ser du istället tre bokstäver.\nDin uppgift då är att välja den korrekta första bokstaven i Namnet eller Yrket till personen som visas.\n\nNär du ser ett kors på skärmen så ska du bara titta på det.\nEfter varje bildvisning där du väljer första bokstaven så kommer korset i mitten av skärmen att övergå till en cirkel under en kort stund.\nTryck så snabbt du kan på en av knapparna när du ser Cirkeln.\n \n\nSvara på varje bild med hjälp av följande knappar:\n1 (pekfinger) = VÄNSTER       \n2 (långfinger) = MITTEN\n3 (ringfinger) = HÖGER\n\nVi vet att det är en svår uppgift så gör så gott du kan och lycka till!\n\nTryck med pekfingret och meddela när du är redo att börja.\n',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_0 = keyboard.Keyboard()

# Initialize components for Routine "Wait_fMRI"
Wait_fMRIClock = core.Clock()
polygon_2 = visual.ShapeStim(
    win=win, name='polygon_2', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.001,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Namn_Info"
Namn_InfoClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='NAMN',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
polygon_5 = visual.ShapeStim(
    win=win, name='polygon_5', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.001,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "Encoding_trial"
Encoding_trialClock = core.Clock()
key_resp_1 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.125), size=(0.743, 0.750),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text=None,
    font='Open Sans',
    pos=(0, -0.375), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
jitter = np.arange(2.5, 10, .25)
shuffle(jitter)



# Initialize components for Routine "fix_cross"
fix_crossClock = core.Clock()
polygon_6 = visual.ShapeStim(
    win=win, name='polygon_6', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.001,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "ImmediateRecall_trial"
ImmediateRecall_trialClock = core.Clock()
key_resp_ImmediateRecall = keyboard.Keyboard()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.125), size=(0.743, 0.750),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(0, -0.375), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fix_cross_circle"
fix_cross_circleClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
Circle = visual.ImageStim(
    win=win,
    name='Circle', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_Circle = keyboard.Keyboard()

# Initialize components for Routine "Proffession_info"
Proffession_infoClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='YRKE',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
polygon_4 = visual.ShapeStim(
    win=win, name='polygon_4', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.001,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "Encoding_trial"
Encoding_trialClock = core.Clock()
key_resp_1 = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.125), size=(0.743, 0.750),
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_4 = visual.TextStim(win=win, name='text_4',
    text=None,
    font='Open Sans',
    pos=(0, -0.375), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
jitter = np.arange(2.5, 10, .25)
shuffle(jitter)



# Initialize components for Routine "fix_cross"
fix_crossClock = core.Clock()
polygon_6 = visual.ShapeStim(
    win=win, name='polygon_6', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.001,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)

# Initialize components for Routine "ImmediateRecall_trial"
ImmediateRecall_trialClock = core.Clock()
key_resp_ImmediateRecall = keyboard.Keyboard()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.125), size=(0.743, 0.750),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Open Sans',
    pos=(0, -0.375), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "fix_cross_circle"
fix_cross_circleClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.1, 0.1),
    ori=0.0, pos=(0, 0),
    lineWidth=0.1,     colorSpace='rgb',  lineColor=None, fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
Circle = visual.ImageStim(
    win=win,
    name='Circle', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.1, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
key_resp_Circle = keyboard.Keyboard()

# Initialize components for Routine "Finished"
FinishedClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Bra jobbat!\n\nDu har slutfört uppgiften. \nFortsätt ligga stilla så kommer vi prata med dig alldeles strax.',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_0.keys = []
key_resp_0.rt = []
_key_resp_0_allKeys = []
# keep track of which components have finished
InstructionsComponents = [text, key_resp_0]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_0* updates
    waitOnFlip = False
    if key_resp_0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_0.frameNStart = frameN  # exact frame index
        key_resp_0.tStart = t  # local t and not account for scr refresh
        key_resp_0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_0, 'tStartRefresh')  # time at next scr refresh
        key_resp_0.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_0.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_0.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_0.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_0.getKeys(keyList=['1', '2', '3', 'space'], waitRelease=False)
        _key_resp_0_allKeys.extend(theseKeys)
        if len(_key_resp_0_allKeys):
            key_resp_0.keys = _key_resp_0_allKeys[-1].name  # just the last key pressed
            key_resp_0.rt = _key_resp_0_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Wait_fMRI"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
Wait_fMRIComponents = [polygon_2, key_resp]
for thisComponent in Wait_fMRIComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Wait_fMRIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Wait_fMRI"-------
while continueRoutine:
    # get current time
    t = Wait_fMRIClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Wait_fMRIClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
    if (key_resp.keys) == 's':
        core.wait(15)
        continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Wait_fMRIComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Wait_fMRI"-------
for thisComponent in Wait_fMRIComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Wait_fMRI" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Namn_Info"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
Namn_InfoComponents = [text_8, polygon_5]
for thisComponent in Namn_InfoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Namn_InfoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Namn_Info"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Namn_InfoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Namn_InfoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    if text_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_8.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_8.tStop = t  # not accounting for scr refresh
            text_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
            text_8.setAutoDraw(False)
    
    # *polygon_5* updates
    if polygon_5.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        polygon_5.frameNStart = frameN  # exact frame index
        polygon_5.tStart = t  # local t and not account for scr refresh
        polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
        polygon_5.setAutoDraw(True)
    if polygon_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_5.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_5.tStop = t  # not accounting for scr refresh
            polygon_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_5, 'tStopRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Namn_InfoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Namn_Info"-------
for thisComponent in Namn_InfoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
thisExp.addData('polygon_5.started', polygon_5.tStartRefresh)
thisExp.addData('polygon_5.stopped', polygon_5.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Name_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TrialRows.xlsx'),
    seed=None, name='Name_trials')
thisExp.addLoop(Name_trials)  # add the loop to the experiment
thisName_trial = Name_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisName_trial.rgb)
if thisName_trial != None:
    for paramName in thisName_trial:
        exec('{} = thisName_trial[paramName]'.format(paramName))

for thisName_trial in Name_trials:
    currentLoop = Name_trials
    # abbreviate parameter names if possible (e.g. rgb = thisName_trial.rgb)
    if thisName_trial != None:
        for paramName in thisName_trial:
            exec('{} = thisName_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Encoding_Name = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Encoding.xlsx', selection=TrialRows_Name),
        seed=None, name='Encoding_Name')
    thisExp.addLoop(Encoding_Name)  # add the loop to the experiment
    thisEncoding_Name = Encoding_Name.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEncoding_Name.rgb)
    if thisEncoding_Name != None:
        for paramName in thisEncoding_Name:
            exec('{} = thisEncoding_Name[paramName]'.format(paramName))
    
    for thisEncoding_Name in Encoding_Name:
        currentLoop = Encoding_Name
        # abbreviate parameter names if possible (e.g. rgb = thisEncoding_Name.rgb)
        if thisEncoding_Name != None:
            for paramName in thisEncoding_Name:
                exec('{} = thisEncoding_Name[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Encoding_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        key_resp_1.keys = []
        key_resp_1.rt = []
        _key_resp_1_allKeys = []
        image.setImage(StimFile)
        text_4.setText('')
        jitter = np.arange(2.5, 10, .25)
        shuffle(jitter)
        thisExp.addData('Jitter', jitter[0])
        
        
        if Name == 0:
            text_4.text = Proffession
        else:
            text_4.text = Name
        # keep track of which components have finished
        Encoding_trialComponents = [key_resp_1, image, text_4]
        for thisComponent in Encoding_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Encoding_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Encoding_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Encoding_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Encoding_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_1* updates
            waitOnFlip = False
            if key_resp_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_1.frameNStart = frameN  # exact frame index
                key_resp_1.tStart = t  # local t and not account for scr refresh
                key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
                key_resp_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_1.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_1.tStop = t  # not accounting for scr refresh
                    key_resp_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_1, 'tStopRefresh')  # time at next scr refresh
                    key_resp_1.status = FINISHED
            if key_resp_1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_1.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_1_allKeys.extend(theseKeys)
                if len(_key_resp_1_allKeys):
                    key_resp_1.keys = _key_resp_1_allKeys[-1].name  # just the last key pressed
                    key_resp_1.rt = _key_resp_1_allKeys[-1].rt
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Encoding_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Encoding_trial"-------
        for thisComponent in Encoding_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_1.keys in ['', [], None]:  # No response was made
            key_resp_1.keys = None
        Encoding_Name.addData('key_resp_1.keys',key_resp_1.keys)
        if key_resp_1.keys != None:  # we had a response
            Encoding_Name.addData('key_resp_1.rt', key_resp_1.rt)
        Encoding_Name.addData('key_resp_1.started', key_resp_1.tStartRefresh)
        Encoding_Name.addData('key_resp_1.stopped', key_resp_1.tStopRefresh)
        Encoding_Name.addData('image.started', image.tStartRefresh)
        Encoding_Name.addData('image.stopped', image.tStopRefresh)
        Encoding_Name.addData('text_4.started', text_4.tStartRefresh)
        Encoding_Name.addData('text_4.stopped', text_4.tStopRefresh)
        
        # ------Prepare to start Routine "fix_cross"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fix_crossComponents = [polygon_6]
        for thisComponent in fix_crossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross"-------
        while continueRoutine:
            # get current time
            t = fix_crossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_crossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_6* updates
            if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_6.frameNStart = frameN  # exact frame index
                polygon_6.tStart = t  # local t and not account for scr refresh
                polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                polygon_6.setAutoDraw(True)
            if polygon_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_6.tStartRefresh + jitter[0]-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_6.tStop = t  # not accounting for scr refresh
                    polygon_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
                    polygon_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross"-------
        for thisComponent in fix_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Encoding_Name.addData('polygon_6.started', polygon_6.tStartRefresh)
        Encoding_Name.addData('polygon_6.stopped', polygon_6.tStopRefresh)
        # the Routine "fix_cross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Encoding_Name'
    
    
    # set up handler to look after randomisation of conditions etc
    ImmediateRecall_Name = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Encoding.xlsx', selection=TrialRows_Name),
        seed=None, name='ImmediateRecall_Name')
    thisExp.addLoop(ImmediateRecall_Name)  # add the loop to the experiment
    thisImmediateRecall_Name = ImmediateRecall_Name.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisImmediateRecall_Name.rgb)
    if thisImmediateRecall_Name != None:
        for paramName in thisImmediateRecall_Name:
            exec('{} = thisImmediateRecall_Name[paramName]'.format(paramName))
    
    for thisImmediateRecall_Name in ImmediateRecall_Name:
        currentLoop = ImmediateRecall_Name
        # abbreviate parameter names if possible (e.g. rgb = thisImmediateRecall_Name.rgb)
        if thisImmediateRecall_Name != None:
            for paramName in thisImmediateRecall_Name:
                exec('{} = thisImmediateRecall_Name[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ImmediateRecall_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        key_resp_ImmediateRecall.keys = []
        key_resp_ImmediateRecall.rt = []
        _key_resp_ImmediateRecall_allKeys = []
        image_3.setImage(StimFile)
        text_6.setText(Letter1 + '\t' * 6 + Letter2 + '\t' * 6 + Letter3)
        jitter = np.arange(2.5, 10, .25)
        shuffle(jitter)
        thisExp.addData('Jitter', jitter[0])
        circlestart = (jitter[0]/2)-0.5
        # keep track of which components have finished
        ImmediateRecall_trialComponents = [key_resp_ImmediateRecall, image_3, text_6]
        for thisComponent in ImmediateRecall_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ImmediateRecall_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ImmediateRecall_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ImmediateRecall_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ImmediateRecall_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_ImmediateRecall* updates
            waitOnFlip = False
            if key_resp_ImmediateRecall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_ImmediateRecall.frameNStart = frameN  # exact frame index
                key_resp_ImmediateRecall.tStart = t  # local t and not account for scr refresh
                key_resp_ImmediateRecall.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_ImmediateRecall, 'tStartRefresh')  # time at next scr refresh
                key_resp_ImmediateRecall.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_ImmediateRecall.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_ImmediateRecall.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_ImmediateRecall.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_ImmediateRecall.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_ImmediateRecall.tStop = t  # not accounting for scr refresh
                    key_resp_ImmediateRecall.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_ImmediateRecall, 'tStopRefresh')  # time at next scr refresh
                    key_resp_ImmediateRecall.status = FINISHED
            if key_resp_ImmediateRecall.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_ImmediateRecall.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_ImmediateRecall_allKeys.extend(theseKeys)
                if len(_key_resp_ImmediateRecall_allKeys):
                    key_resp_ImmediateRecall.keys = _key_resp_ImmediateRecall_allKeys[-1].name  # just the last key pressed
                    key_resp_ImmediateRecall.rt = _key_resp_ImmediateRecall_allKeys[-1].rt
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(False)
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ImmediateRecall_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ImmediateRecall_trial"-------
        for thisComponent in ImmediateRecall_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_ImmediateRecall.keys in ['', [], None]:  # No response was made
            key_resp_ImmediateRecall.keys = None
        ImmediateRecall_Name.addData('key_resp_ImmediateRecall.keys',key_resp_ImmediateRecall.keys)
        if key_resp_ImmediateRecall.keys != None:  # we had a response
            ImmediateRecall_Name.addData('key_resp_ImmediateRecall.rt', key_resp_ImmediateRecall.rt)
        ImmediateRecall_Name.addData('key_resp_ImmediateRecall.started', key_resp_ImmediateRecall.tStartRefresh)
        ImmediateRecall_Name.addData('key_resp_ImmediateRecall.stopped', key_resp_ImmediateRecall.tStopRefresh)
        ImmediateRecall_Name.addData('image_3.started', image_3.tStartRefresh)
        ImmediateRecall_Name.addData('image_3.stopped', image_3.tStopRefresh)
        ImmediateRecall_Name.addData('text_6.started', text_6.tStartRefresh)
        ImmediateRecall_Name.addData('text_6.stopped', text_6.tStopRefresh)
        
        # ------Prepare to start Routine "fix_cross_circle"-------
        continueRoutine = True
        # update component parameters for each repeat
        Circle.setImage('Circle.png')
        key_resp_Circle.keys = []
        key_resp_Circle.rt = []
        _key_resp_Circle_allKeys = []
        # keep track of which components have finished
        fix_cross_circleComponents = [polygon, Circle, key_resp_Circle]
        for thisComponent in fix_cross_circleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_cross_circleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross_circle"-------
        while continueRoutine:
            # get current time
            t = fix_cross_circleClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_cross_circleClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + jitter[0]-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # *Circle* updates
            if Circle.status == NOT_STARTED and tThisFlip >= circlestart-frameTolerance:
                # keep track of start time/frame for later
                Circle.frameNStart = frameN  # exact frame index
                Circle.tStart = t  # local t and not account for scr refresh
                Circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle, 'tStartRefresh')  # time at next scr refresh
                Circle.setAutoDraw(True)
            if Circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle.tStop = t  # not accounting for scr refresh
                    Circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Circle, 'tStopRefresh')  # time at next scr refresh
                    Circle.setAutoDraw(False)
            
            # *key_resp_Circle* updates
            waitOnFlip = False
            if key_resp_Circle.status == NOT_STARTED and tThisFlip >= circlestart-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Circle.frameNStart = frameN  # exact frame index
                key_resp_Circle.tStart = t  # local t and not account for scr refresh
                key_resp_Circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Circle, 'tStartRefresh')  # time at next scr refresh
                key_resp_Circle.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_Circle.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_Circle.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_Circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_Circle.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_Circle.tStop = t  # not accounting for scr refresh
                    key_resp_Circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_Circle, 'tStopRefresh')  # time at next scr refresh
                    key_resp_Circle.status = FINISHED
            if key_resp_Circle.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_Circle.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_Circle_allKeys.extend(theseKeys)
                if len(_key_resp_Circle_allKeys):
                    key_resp_Circle.keys = _key_resp_Circle_allKeys[-1].name  # just the last key pressed
                    key_resp_Circle.rt = _key_resp_Circle_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_cross_circleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross_circle"-------
        for thisComponent in fix_cross_circleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ImmediateRecall_Name.addData('Circle.started', Circle.tStartRefresh)
        ImmediateRecall_Name.addData('Circle.stopped', Circle.tStopRefresh)
        # check responses
        if key_resp_Circle.keys in ['', [], None]:  # No response was made
            key_resp_Circle.keys = None
        ImmediateRecall_Name.addData('key_resp_Circle.keys',key_resp_Circle.keys)
        if key_resp_Circle.keys != None:  # we had a response
            ImmediateRecall_Name.addData('key_resp_Circle.rt', key_resp_Circle.rt)
        ImmediateRecall_Name.addData('key_resp_Circle.started', key_resp_Circle.tStartRefresh)
        ImmediateRecall_Name.addData('key_resp_Circle.stopped', key_resp_Circle.tStopRefresh)
        # the Routine "fix_cross_circle" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'ImmediateRecall_Name'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Name_trials'


# ------Prepare to start Routine "Proffession_info"-------
continueRoutine = True
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
Proffession_infoComponents = [text_9, polygon_4]
for thisComponent in Proffession_infoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Proffession_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Proffession_info"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Proffession_infoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Proffession_infoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    if text_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_9.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            text_9.tStop = t  # not accounting for scr refresh
            text_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
            text_9.setAutoDraw(False)
    
    # *polygon_4* updates
    if polygon_4.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        polygon_4.frameNStart = frameN  # exact frame index
        polygon_4.tStart = t  # local t and not account for scr refresh
        polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
        polygon_4.setAutoDraw(True)
    if polygon_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_4.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_4.tStop = t  # not accounting for scr refresh
            polygon_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Proffession_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Proffession_info"-------
for thisComponent in Proffession_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
thisExp.addData('polygon_4.started', polygon_4.tStartRefresh)
thisExp.addData('polygon_4.stopped', polygon_4.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Proffession_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('TrialRows.xlsx'),
    seed=None, name='Proffession_trials')
thisExp.addLoop(Proffession_trials)  # add the loop to the experiment
thisProffession_trial = Proffession_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisProffession_trial.rgb)
if thisProffession_trial != None:
    for paramName in thisProffession_trial:
        exec('{} = thisProffession_trial[paramName]'.format(paramName))

for thisProffession_trial in Proffession_trials:
    currentLoop = Proffession_trials
    # abbreviate parameter names if possible (e.g. rgb = thisProffession_trial.rgb)
    if thisProffession_trial != None:
        for paramName in thisProffession_trial:
            exec('{} = thisProffession_trial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Encoding_Proffession = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Encoding.xlsx', selection=TrialRows_Proffession),
        seed=None, name='Encoding_Proffession')
    thisExp.addLoop(Encoding_Proffession)  # add the loop to the experiment
    thisEncoding_Proffession = Encoding_Proffession.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisEncoding_Proffession.rgb)
    if thisEncoding_Proffession != None:
        for paramName in thisEncoding_Proffession:
            exec('{} = thisEncoding_Proffession[paramName]'.format(paramName))
    
    for thisEncoding_Proffession in Encoding_Proffession:
        currentLoop = Encoding_Proffession
        # abbreviate parameter names if possible (e.g. rgb = thisEncoding_Proffession.rgb)
        if thisEncoding_Proffession != None:
            for paramName in thisEncoding_Proffession:
                exec('{} = thisEncoding_Proffession[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Encoding_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        key_resp_1.keys = []
        key_resp_1.rt = []
        _key_resp_1_allKeys = []
        image.setImage(StimFile)
        text_4.setText('')
        jitter = np.arange(2.5, 10, .25)
        shuffle(jitter)
        thisExp.addData('Jitter', jitter[0])
        
        
        if Name == 0:
            text_4.text = Proffession
        else:
            text_4.text = Name
        # keep track of which components have finished
        Encoding_trialComponents = [key_resp_1, image, text_4]
        for thisComponent in Encoding_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Encoding_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Encoding_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Encoding_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Encoding_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_1* updates
            waitOnFlip = False
            if key_resp_1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_1.frameNStart = frameN  # exact frame index
                key_resp_1.tStart = t  # local t and not account for scr refresh
                key_resp_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_1, 'tStartRefresh')  # time at next scr refresh
                key_resp_1.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_1.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_1.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_1.tStop = t  # not accounting for scr refresh
                    key_resp_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_1, 'tStopRefresh')  # time at next scr refresh
                    key_resp_1.status = FINISHED
            if key_resp_1.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_1.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_1_allKeys.extend(theseKeys)
                if len(_key_resp_1_allKeys):
                    key_resp_1.keys = _key_resp_1_allKeys[-1].name  # just the last key pressed
                    key_resp_1.rt = _key_resp_1_allKeys[-1].rt
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Encoding_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Encoding_trial"-------
        for thisComponent in Encoding_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_1.keys in ['', [], None]:  # No response was made
            key_resp_1.keys = None
        Encoding_Proffession.addData('key_resp_1.keys',key_resp_1.keys)
        if key_resp_1.keys != None:  # we had a response
            Encoding_Proffession.addData('key_resp_1.rt', key_resp_1.rt)
        Encoding_Proffession.addData('key_resp_1.started', key_resp_1.tStartRefresh)
        Encoding_Proffession.addData('key_resp_1.stopped', key_resp_1.tStopRefresh)
        Encoding_Proffession.addData('image.started', image.tStartRefresh)
        Encoding_Proffession.addData('image.stopped', image.tStopRefresh)
        Encoding_Proffession.addData('text_4.started', text_4.tStartRefresh)
        Encoding_Proffession.addData('text_4.stopped', text_4.tStopRefresh)
        
        # ------Prepare to start Routine "fix_cross"-------
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        fix_crossComponents = [polygon_6]
        for thisComponent in fix_crossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross"-------
        while continueRoutine:
            # get current time
            t = fix_crossClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_crossClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_6* updates
            if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_6.frameNStart = frameN  # exact frame index
                polygon_6.tStart = t  # local t and not account for scr refresh
                polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                polygon_6.setAutoDraw(True)
            if polygon_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_6.tStartRefresh + jitter[0]-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_6.tStop = t  # not accounting for scr refresh
                    polygon_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
                    polygon_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross"-------
        for thisComponent in fix_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Encoding_Proffession.addData('polygon_6.started', polygon_6.tStartRefresh)
        Encoding_Proffession.addData('polygon_6.stopped', polygon_6.tStopRefresh)
        # the Routine "fix_cross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'Encoding_Proffession'
    
    
    # set up handler to look after randomisation of conditions etc
    ImmediateRecall_Proffession = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Encoding.xlsx', selection=TrialRows_Proffession),
        seed=None, name='ImmediateRecall_Proffession')
    thisExp.addLoop(ImmediateRecall_Proffession)  # add the loop to the experiment
    thisImmediateRecall_Proffession = ImmediateRecall_Proffession.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisImmediateRecall_Proffession.rgb)
    if thisImmediateRecall_Proffession != None:
        for paramName in thisImmediateRecall_Proffession:
            exec('{} = thisImmediateRecall_Proffession[paramName]'.format(paramName))
    
    for thisImmediateRecall_Proffession in ImmediateRecall_Proffession:
        currentLoop = ImmediateRecall_Proffession
        # abbreviate parameter names if possible (e.g. rgb = thisImmediateRecall_Proffession.rgb)
        if thisImmediateRecall_Proffession != None:
            for paramName in thisImmediateRecall_Proffession:
                exec('{} = thisImmediateRecall_Proffession[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ImmediateRecall_trial"-------
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        key_resp_ImmediateRecall.keys = []
        key_resp_ImmediateRecall.rt = []
        _key_resp_ImmediateRecall_allKeys = []
        image_3.setImage(StimFile)
        text_6.setText(Letter1 + '\t' * 6 + Letter2 + '\t' * 6 + Letter3)
        jitter = np.arange(2.5, 10, .25)
        shuffle(jitter)
        thisExp.addData('Jitter', jitter[0])
        circlestart = (jitter[0]/2)-0.5
        # keep track of which components have finished
        ImmediateRecall_trialComponents = [key_resp_ImmediateRecall, image_3, text_6]
        for thisComponent in ImmediateRecall_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ImmediateRecall_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ImmediateRecall_trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ImmediateRecall_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ImmediateRecall_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp_ImmediateRecall* updates
            waitOnFlip = False
            if key_resp_ImmediateRecall.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_ImmediateRecall.frameNStart = frameN  # exact frame index
                key_resp_ImmediateRecall.tStart = t  # local t and not account for scr refresh
                key_resp_ImmediateRecall.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_ImmediateRecall, 'tStartRefresh')  # time at next scr refresh
                key_resp_ImmediateRecall.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_ImmediateRecall.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_ImmediateRecall.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_ImmediateRecall.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_ImmediateRecall.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_ImmediateRecall.tStop = t  # not accounting for scr refresh
                    key_resp_ImmediateRecall.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_ImmediateRecall, 'tStopRefresh')  # time at next scr refresh
                    key_resp_ImmediateRecall.status = FINISHED
            if key_resp_ImmediateRecall.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_ImmediateRecall.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_ImmediateRecall_allKeys.extend(theseKeys)
                if len(_key_resp_ImmediateRecall_allKeys):
                    key_resp_ImmediateRecall.keys = _key_resp_ImmediateRecall_allKeys[-1].name  # just the last key pressed
                    key_resp_ImmediateRecall.rt = _key_resp_ImmediateRecall_allKeys[-1].rt
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(False)
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            if text_6.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_6.tStartRefresh + 4-frameTolerance:
                    # keep track of stop time/frame for later
                    text_6.tStop = t  # not accounting for scr refresh
                    text_6.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                    text_6.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ImmediateRecall_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ImmediateRecall_trial"-------
        for thisComponent in ImmediateRecall_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_ImmediateRecall.keys in ['', [], None]:  # No response was made
            key_resp_ImmediateRecall.keys = None
        ImmediateRecall_Proffession.addData('key_resp_ImmediateRecall.keys',key_resp_ImmediateRecall.keys)
        if key_resp_ImmediateRecall.keys != None:  # we had a response
            ImmediateRecall_Proffession.addData('key_resp_ImmediateRecall.rt', key_resp_ImmediateRecall.rt)
        ImmediateRecall_Proffession.addData('key_resp_ImmediateRecall.started', key_resp_ImmediateRecall.tStartRefresh)
        ImmediateRecall_Proffession.addData('key_resp_ImmediateRecall.stopped', key_resp_ImmediateRecall.tStopRefresh)
        ImmediateRecall_Proffession.addData('image_3.started', image_3.tStartRefresh)
        ImmediateRecall_Proffession.addData('image_3.stopped', image_3.tStopRefresh)
        ImmediateRecall_Proffession.addData('text_6.started', text_6.tStartRefresh)
        ImmediateRecall_Proffession.addData('text_6.stopped', text_6.tStopRefresh)
        
        # ------Prepare to start Routine "fix_cross_circle"-------
        continueRoutine = True
        # update component parameters for each repeat
        Circle.setImage('Circle.png')
        key_resp_Circle.keys = []
        key_resp_Circle.rt = []
        _key_resp_Circle_allKeys = []
        # keep track of which components have finished
        fix_cross_circleComponents = [polygon, Circle, key_resp_Circle]
        for thisComponent in fix_cross_circleComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        fix_cross_circleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "fix_cross_circle"-------
        while continueRoutine:
            # get current time
            t = fix_cross_circleClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=fix_cross_circleClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon* updates
            if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                polygon.setAutoDraw(True)
            if polygon.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon.tStartRefresh + jitter[0]-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                    polygon.setAutoDraw(False)
            
            # *Circle* updates
            if Circle.status == NOT_STARTED and tThisFlip >= circlestart-frameTolerance:
                # keep track of start time/frame for later
                Circle.frameNStart = frameN  # exact frame index
                Circle.tStart = t  # local t and not account for scr refresh
                Circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle, 'tStartRefresh')  # time at next scr refresh
                Circle.setAutoDraw(True)
            if Circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Circle.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Circle.tStop = t  # not accounting for scr refresh
                    Circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Circle, 'tStopRefresh')  # time at next scr refresh
                    Circle.setAutoDraw(False)
            
            # *key_resp_Circle* updates
            waitOnFlip = False
            if key_resp_Circle.status == NOT_STARTED and tThisFlip >= circlestart-frameTolerance:
                # keep track of start time/frame for later
                key_resp_Circle.frameNStart = frameN  # exact frame index
                key_resp_Circle.tStart = t  # local t and not account for scr refresh
                key_resp_Circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_Circle, 'tStartRefresh')  # time at next scr refresh
                key_resp_Circle.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_Circle.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_Circle.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_Circle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_Circle.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_Circle.tStop = t  # not accounting for scr refresh
                    key_resp_Circle.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_Circle, 'tStopRefresh')  # time at next scr refresh
                    key_resp_Circle.status = FINISHED
            if key_resp_Circle.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_Circle.getKeys(keyList=['1', '2', '3'], waitRelease=False)
                _key_resp_Circle_allKeys.extend(theseKeys)
                if len(_key_resp_Circle_allKeys):
                    key_resp_Circle.keys = _key_resp_Circle_allKeys[-1].name  # just the last key pressed
                    key_resp_Circle.rt = _key_resp_Circle_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fix_cross_circleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fix_cross_circle"-------
        for thisComponent in fix_cross_circleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ImmediateRecall_Proffession.addData('Circle.started', Circle.tStartRefresh)
        ImmediateRecall_Proffession.addData('Circle.stopped', Circle.tStopRefresh)
        # check responses
        if key_resp_Circle.keys in ['', [], None]:  # No response was made
            key_resp_Circle.keys = None
        ImmediateRecall_Proffession.addData('key_resp_Circle.keys',key_resp_Circle.keys)
        if key_resp_Circle.keys != None:  # we had a response
            ImmediateRecall_Proffession.addData('key_resp_Circle.rt', key_resp_Circle.rt)
        ImmediateRecall_Proffession.addData('key_resp_Circle.started', key_resp_Circle.tStartRefresh)
        ImmediateRecall_Proffession.addData('key_resp_Circle.stopped', key_resp_Circle.tStopRefresh)
        # the Routine "fix_cross_circle" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'ImmediateRecall_Proffession'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Proffession_trials'


# ------Prepare to start Routine "Finished"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
FinishedComponents = [text_2]
for thisComponent in FinishedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FinishedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Finished"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = FinishedClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FinishedClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinishedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finished"-------
for thisComponent in FinishedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
