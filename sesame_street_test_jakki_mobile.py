import viz
import vizact
import oculus
import vizconnect
import vizfx

#Features to add:
#1) Make runnable from same file for both PPT and mobile
#5) Make GUI slider for scaling both characters
#6) Test looking@ function, bones might not work for this

debug = False

viz.setOption('viz.glFinish', 1)
viz.setMultiSample(8)

vizconnect.go('keyboard_sesame_street_config_fixed.py')

#####Turn Cluster Master Off in Vizard#####

viz.MainView.getHeadLight().disable()

if debug:
	world = vizfx.addChild('dojo.osgb')
	viz.setDebugSound3D(viz.ON)
else:
	print 'Loading lab room model, this might take a while...'
	world = vizfx.addChild('Resources/labroom.osgb')
	light = vizfx.addDirectionalLight()
	light.setEuler([0,90,0])
	
	viz.mouse.setTrap(viz.ON) 
	#Make the mouse invisible. 
	viz.mouse.setVisible(viz.OFF)

print 'Loading avatar models, this might also take a while...'

elmo = vizfx.addAvatar('Resources/Elmo/elmo.cfg')
elmo.setScale([1.2,1.2,1.2])
elmo.setPosition([-1,0,1])
elmo.setEuler([120,0,0])
elmo.state(1)

grover = vizfx.addAvatar('Resources/Grover/grover.cfg')
grover.setScale([1.2,1.2,1.2])
grover.setPosition([1,0,1.5])
grover.setEuler([225,0,0])
grover.state(1)

grover_greet_sound = grover.playsound('Resources/Sounds/grover_hello_furry.wav', viz.STOP)
grover_dance_sound = grover.playsound('Resources/Sounds/grover_dance.wav', viz.STOP)

def groverGreet():
	grover.execute(2, delay_out=1.5)
	grover_greet_sound.play()
	
def letsDance():
	grover_dance_sound.play()
	grover.execute(2, delay_out=1.5)
	elmo.execute(3, delay_out=1.5)
	
vizact.onkeydown('1', groverGreet)
vizact.onkeydown('2', letsDance)

