#Created by Cody Karutz, 2014

import viz
import vizact
import oculus
import vizconnect
import vizfx
import vizinput
import viztask
import time

#Features to add:
#1) Make runnable from same file for both PPT and mobile
#5) Make GUI slider for scaling both characters
#6) Test looking@ function, bones might not work for this
##########################################################
#DONE# 1) Gui selection for responsive vs. non responsive condition
#2) Responsive condition: Record euler of grovers head, record when child responds (keypress 4), 
#	random array of times at 30 second intervals
#3) Non-responsive condition: Use recorded euler to set grovers head, (don't record euler)
#DONE# 4) Reset heading
DEBUG = False
PPT1 = True

INPUTBOXPOS = [2500,500]

WAIT_TIME = .1
conditionChoices = ['Non-responsive', 'Responsive']
if PPT1:
	SUBJECT_NUMBER = vizinput.input('Subject number: ', pos=INPUTBOXPOS)
	RESPONSIVE = vizinput.choose('Condition: ', conditionChoices, pos=INPUTBOXPOS)
else:
	SUBJECT_NUMBER = vizinput.input('Subject number: ')
	RESPONSIVE = vizinput.choose('Condition: ', conditionChoices)


HEADING_RESET = False;

startTime = time.time()
randomTimes = []

def initializeChildTrackingData():
	global tracking_data
	tracking_data = open('./data/' + str(SUBJECT_NUMBER)+'_child_tracking.txt', 'a')
	tracking_data.write('Subject number: ' + str(SUBJECT_NUMBER) + '\n')
	global action_data
	action_data = open('./data/' + str(SUBJECT_NUMBER) + '_chid_actions.txt', 'a')
	action_data.write('Subject number: ' + str(SUBJECT_NUMBER) + '\n')


def initializeResponsiveTrackingData():
	global euler_data
	euler_data = open('./data/responsive/' + str(SUBJECT_NUMBER) +'_euler_data.txt', 'a')
	euler_data.write('START TIME: ' + str(startTime))

def getResponsiveTrackingData():
	global grover
	global ghost
	global tracking_data
	global euler_data
	curr_time = time.time()
	elapsed_time = curr_time - startTime
	ghost.lookAt(viz.MainView.getPosition())
	groverEuler = ghost.getEuler()[0]

	orientation = viz.MainView.getEuler()
	position = viz.MainView.getPosition()
	#Make a string out of the data.
	eulerData = str(groverEuler) + '\t' + str(elapsed_time) + '\n'
	euler_data.write(eulerData)
	data = str(orientation) + '\t' + str(position) + '\t' + str(elapsed_time)+'\n' 
	#Write it to the tracking file.
	tracking_data.write(data)

def getYokingData():
	global euler_data
	import os, os.path
	logdir = './data/responsive/'
	listOfFiles = [ f for f in os.listdir(logdir) if os.path.isfile(os.path.join(logdir,f)) ]
	euler_data = open(logdir + max(listOfFiles, key = lambda x: os.path.getctime(logdir + x))) #HOW TO KNOW WHICH SUBJECT"S DATA TO READ??? -GD
																#DO WE WANT THIS AS A CONSTANT OR TO BE INPUTTED 
																#AT THE BEGINNING OF THE EXPERIMENT

def getUnresponsiveDataAndUpdateGrover(): #STILL NEED TO RECORD CHILD POSITION DATA
	global euler_data
	data = euler_data.readline()
	euler = data.split('	', 1)[0]
	global grover
	grover.setEuler([float(euler), 0, 0])

def recordKeyDown():
	curr_time = time.time()
	elapsed_time = curr_time - startTime
	global action_data
	data = "Child clapped at" + str(elapsed_time)+'\n'
	action_data.write(data)

def init():
	viz.setOption('viz.glFinish', 1)
	viz.setMultiSample(8)

	if PPT1: 
		vizconnect.go('vizconnect_config_DK2_mirror_PPT1_nonOH.py')
		import vizsonic
		vizsonic.setReverb(6.0, 0.2, 0.5, 0.9, 0.0)
		vizsonic.setSimulatedRoomRadius(6.5,4.5)
	else:
		vizconnect.go('vizconnect_mobile_keyboard.py')

	viz.MainView.getHeadLight().disable()

	if DEBUG:
		world = vizfx.addChild('dojo.osgb')
		viz.setDebugSound3D(viz.ON)
	else:
		print 'Loading lab room model, this might take a while...'
		world = vizfx.addChild('Resources/labroom.osgb')
		#Adjust these 
		world.setScale([0.8,0.75,0.8])
		world.setPosition([-0.4,0,-0.4])
		#Directional Light
		light = vizfx.addDirectionalLight()
		light.setEuler([0,90,0])
		viz.mouse.setTrap(viz.ON) 
		viz.mouse.setVisible(viz.OFF)

	print 'Loading avatar models, this might also take a while...'

def addCharacters():
	global grover
	global ghost
	grover = vizfx.addAvatar('Resources/Grover/grover.cfg')
	ghost = vizfx.addAvatar('Resources/Grover/grover.cfg')
	ghost.visible(viz.OFF)
	grover.setScale([.856,.856,.856]) #average 5 year old height ~107 cm and grover model hieght is ~125 cm (.856 = 107/125)
	grover.setPosition([1.2,0,0.6])
	grover.state(1)
	grover.setEuler([180,0,0])

#	global grover_greet_sound
#	#grover_greet_sound = grover.playsound('Resources/Sounds/grover_hello_furry.wav', viz.STOP)
#	grover_greet_sound.volume(0.5)
#	global grover_dance_sound	
#	#grover_dance_sound = grover.playsound('Resources/Sounds/grover_dance.wav', viz.STOP)
#	grover_dance_sound.volume(0.5)
#	global blip
	#blip = grover.playsound('Resources/Sounds/blip.wav', viz.STOP)

def initResponsiveness():
	if RESPONSIVE:
		grover.billboard(viz.BILLBOARD_YAXIS)
	else:
		grover.billboard(viz.OFF)

def responsiveExperiment():
	groverEuler = []
	timeStamps = []
	childPos = [[[]]]
	startTime = viz.tick()
	global grover
	tracker = vizconnect.getTracker('merged')
	viz.waitTime(WAIT_TIME)
	
def getTrackingData():
	elapsedTime = viz.tick() - startTime
	timeStamps.append(elapsedTime)
#		euler = grover.getEuler[0]
	groverEuler.append(grover.getEuler()[0])
	print groverEuler
	currPos = tracker.getPosition()
	currEuler = tracker.getEuler()

#		childPos.append()
		
def setKeyPresses():
	vizact.onkeydown('1', groverGreet)
	vizact.onkeydown('2', letsDance)
	vizact.onkeydown('=', scaleUp)
	vizact.onkeydown('-', scaleDown)
	vizact.onkeydown('c', recordKeyDown)


def groverGreet():
	grover.execute(2, delay_out=1.5)
	global grover_greet_sound	
	grover_greet_sound.play()
	
def letsDance():
	global grover_dance_sound
	grover_dance_sound.play()
	grover.execute(2, delay_out=1.5)
	
def scaleUp():
	groverScale = grover.getScale()
	grover.setScale([groverScale[0]+0.1,groverScale[1]+0.1,groverScale[2]+0.1])
	global blip	
	blip.play()
	
def scaleDown():
	groverScale = grover.getScale()
	grover.setScale([groverScale[0]-0.1,groverScale[1]-0.1,groverScale[2]-0.1])
	blip.play()

	
def Main():
	init()
	addCharacters()
	initResponsiveness()
	setKeyPresses()
	initializeChildTrackingData()
	if RESPONSIVE:
		initializeResponsiveTrackingData()
		vizact.onupdate(1, getResponsiveTrackingData)
	else:
		getYokingData()
		vizact.onupdate(1, getUnresponsiveDataAndUpdateGrover)

Main()