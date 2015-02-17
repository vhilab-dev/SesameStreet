#Created by Cody Karutz, 2014

import viz
import vizact
import oculus
import vizconnect
import vizfx

#Features to add:
#1) Make runnable from same file for both PPT and mobile
#5) Make GUI slider for scaling both characters
#6) Test looking@ function, bones might not work for this

DEBUG = False
PPT1 = True
BILLBOARD = False

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

elmo = vizfx.addAvatar('Resources/Elmo/elmo.cfg')
elmo.setScale([1.1,1.1,1.1])
elmo.setPosition([-1.2,0,0.5])
elmo.state(1)
elmo.setEuler([180,0,0])

grover = vizfx.addAvatar('Resources/Grover/grover.cfg')
grover.setScale([1.1,1.1,1.1])
grover.setPosition([1.2,0,0.6])
grover.state(1)
grover.setEuler([180,0,0])

grover_greet_sound = grover.playsound('Resources/Sounds/grover_hello_furry.wav', viz.STOP)
grover_greet_sound.volume(0.5)
grover_dance_sound = grover.playsound('Resources/Sounds/grover_dance.wav', viz.STOP)
grover_dance_sound.volume(0.5)
blip = grover.playsound('Resources/Sounds/blip.wav', viz.STOP)

def groverGreet():
	grover.execute(2, delay_out=1.5)
	grover_greet_sound.play()
	
def letsDance():
	grover_dance_sound.play()
	grover.execute(2, delay_out=1.5)
	elmo.execute(3, delay_out=1.5)
	
def scaleUp():
	groverScale = grover.getScale()
	grover.setScale([groverScale[0]+0.1,groverScale[1]+0.1,groverScale[2]+0.1])
	elmoScale = elmo.getScale()
	elmo.setScale([elmoScale[0]+0.1,elmoScale[1]+0.1,elmoScale[2]+0.1])
	blip.play()
	
def scaleDown():
	groverScale = grover.getScale()
	grover.setScale([groverScale[0]-0.1,groverScale[1]-0.1,groverScale[2]-0.1])
	elmoScale = elmo.getScale()
	elmo.setScale([elmoScale[0]-0.1,elmoScale[1]-0.1,elmoScale[2]-0.1])
	blip.play()
	
def billboardToggle():
	global BILLBOARD
	if BILLBOARD:
		elmo.billboard(viz.OFF)
		grover.billboard(viz.OFF)
		BILLBOARD = False
	else:
		elmo.billboard(viz.BILLBOARD_YAXIS)
		grover.billboard(viz.BILLBOARD_YAXIS)
		BILLBOARD = True
	
vizact.onkeydown('1', groverGreet)
vizact.onkeydown('2', letsDance)
vizact.onkeydown('3', billboardToggle)
vizact.onkeydown('=', scaleUp)
vizact.onkeydown('-', scaleDown)