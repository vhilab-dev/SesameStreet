"""
This module was generated by Vizconnect.
Version: 1.01
Generated on: 2014-09-16 12:34:37.302000
"""

import viz
import vizconnect

#################################
# Parent configuration, if any
#################################

def getParentConfiguration():
	#VC: set the parent configuration
	_parent = ''
	
	#VC: return the parent configuration
	return _parent


#################################
# Pre viz.go() Code
#################################

def preVizGo():
	return True


#################################
# Pre-initialization Code
#################################

def preInit():
	"""Add any code here which should be called after viz.go but before any initializations happen.
	Returned values can be obtained by calling getPreInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Group Code
#################################

def initGroups(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawGroup = vizconnect.getRawGroupDict()
	
	#VC: return values can be modified here
	return None


#################################
# Display Code
#################################

def initDisplays(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawDisplay = vizconnect.getRawDisplayDict()

	#VC: initialize a new display
	_name = 'rift'
	if vizconnect.isPendingInit('display', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set the window for the display
			_window = viz.MainWindow
			
			#VC: make the window visible only for certain clients
			_clusterMask = viz.MASTER
			with viz.cluster.MaskedContext(viz.ALLCLIENTS&~_clusterMask):# hide
				_window.visible(False)
			with viz.cluster.MaskedContext(_clusterMask):# show
				_window.visible(True)
			
			#VC: set the fullscreen monitor
			with viz.cluster.MaskedContext(viz.MASTER):# only for clients with this display
				viz.window.setFullscreenMonitor(1)
				viz.window.setFullscreen(True)
			
			#VC: set some parameters
			autoDetectMonitor = True
			
			#VC: create the raw object
			import oculus
			_window.displayNode = oculus.Rift(window=_window, autoDetectMonitor=autoDetectMonitor)
			viz.window.setFullscreen(True)
			rawDisplay[_name] = _window
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addDisplay(rawDisplay[_name], _name, make='Oculus VR', model='Rift')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getDisplay(_name).setParent(vizconnect.getTracker('merged'))

	#VC: initialize a new display
	_name = 'mirror'
	if vizconnect.isPendingInit('display', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set the window for the display
			_window = viz.addWindow()
			_window.setView(viz.addView())
			
			#VC: set placement with alignment: free
			_window.setPosition(0, 1, mode=viz.WINDOW_NORMALIZED)
			_window.setSize(1, 1, mode=viz.WINDOW_NORMALIZED)
			
			#VC: make the window visible only for certain clients
			_clusterMask = viz.CLIENT1
			with viz.cluster.MaskedContext(viz.ALLCLIENTS&~_clusterMask):# hide
				_window.visible(False)
			with viz.cluster.MaskedContext(_clusterMask):# show
				_window.visible(True)
			
			#VC: set the fullscreen monitor
			with viz.cluster.MaskedContext(viz.CLIENT1):# only for clients with this display
				viz.window.setFullscreenMonitor(2)
				viz.window.setFullscreen(True)
			
			#VC: set some parameters
			VFOV = 60
			aspect = viz.AUTO_COMPUTE
			stereo = viz.OFF
			
			#VC: create the raw object
			_window.fov(VFOV,aspect)
			_window.stereo(stereo)
			rawDisplay[_name] = _window
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addDisplay(rawDisplay[_name], _name, make='Generic', model='Custom Window')
	
		#VC: set the parent of the node
		if initFlag&vizconnect.INIT_PARENTS:
			vizconnect.getDisplay(_name).setParent(vizconnect.getTracker('merged'))

	#VC: return values can be modified here
	return None


#################################
# Tracker Code
#################################

def initTrackers(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTracker = vizconnect.getRawTrackerDict()

	#VC: initialize a new tracker
	_name = 'ppt_left_eye'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			pptHostname = '171.64.33.43'
			markerId = 1
			
			#VC: create the raw object
			vrpn7 = viz.add('vrpn7.dle')
			rawTracker[_name] = vrpn7.addTracker('PPT0@'+pptHostname, markerId-1)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='WorldViz', model='PPT')

	#VC: initialize a new tracker
	_name = 'rift_orientation_tracker'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: create the raw object
			import oculus
			index=0
			sensorList = oculus.getSensors()
			if index < len(sensorList):
				orientationTracker = sensorList[index]
			else:
				viz.logWarn("** WARNING: Oculus VR Rift Orientation Tracker not present.")
				orientationTracker = viz.addGroup()
				orientationTracker.invalidTracker = True
			rawTracker[_name] = orientationTracker
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Oculus VR', model='Rift Orientation Tracker')
	
		#VC: init the mappings for the wrapper
		if initFlag&vizconnect.INIT_WRAPPER_MAPPINGS:
			#VC: on-state mappings
			if initFlag&vizconnect.INIT_MAPPINGS_ON_STATE:
				vizconnect.getTracker(_name).setOnStateEventList([
						vizconnect.onstate(lambda rawInput: rawInput['keyboard'].isButtonDown(19), vizconnect.getTracker(_name).resetHeading),# make=Generic, model=Keyboard, name=keyboard, signal=Key R
				])

	#VC: initialize a new tracker
	_name = 'merged'
	if vizconnect.isPendingInit('tracker', _name, initFlag, initList):
		#VC: request that any dependencies be created
		if initFlag&vizconnect.INIT_INDEPENDENT:
			initTrackers(vizconnect.INIT_INDEPENDENT, ['ppt_left_eye'])
			initTrackers(vizconnect.INIT_INDEPENDENT, ['rift_orientation_tracker'])
	
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			posTracker = vizconnect.getTracker('ppt_left_eye').getNode3d()
			oriTracker = vizconnect.getTracker('rift_orientation_tracker').getNode3d()
			
			#VC: create the raw object
			try:
				raw = viz.mergeLinkable(posTracker, oriTracker)
			except:
				viz.logError('Error **: unable to create merged tracker, providing empty tracker object.')
				raw = viz.addGroup()
				raw.invalidTracker = True
			rawTracker[_name] = raw
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addTracker(rawTracker[_name], _name, make='Virtual', model='Merged')
	
		#VC: init the offsets
		if initFlag&vizconnect.INIT_OFFSETS:
			_link = vizconnect.getTracker(_name).getLink()
			#VC: clear link offsets
			_link.reset(viz.RESET_OPERATORS)
			
			#VC: reset orientation
			_link.preEuler([0, 0, 0], target=viz.LINK_ORI_OP, priority=-20)
			
			#VC: apply offsets
			_link.preTrans([0.0975, -0.08, -0.07])

	#VC: return values can be modified here
	return None


#################################
# Input Code
#################################

def initInputs(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawInput = vizconnect.getRawInputDict()

	#VC: initialize a new input
	_name = 'keyboard'
	if vizconnect.isPendingInit('input', _name, initFlag, initList):
		#VC: init the raw object
		if initFlag&vizconnect.INIT_RAW:
			#VC: set some parameters
			index = 0
			
			#VC: create the raw object
			d = viz.add('directinput.dle')
			device = d.getKeyboardDevices()[index]
			rawInput[_name] = d.addKeyboard(device)
	
		#VC: init the wrapper (DO NOT EDIT)
		if initFlag&vizconnect.INIT_WRAPPERS:
			vizconnect.addInput(rawInput[_name], _name, make='Generic', model='Keyboard')

	#VC: return values can be modified here
	return None


#################################
# Event Code
#################################

def initEvents(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawEvent = vizconnect.getRawEventDict()
	
	#VC: return values can be modified here
	return None


#################################
# Transport Code
#################################

def initTransports(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTransport = vizconnect.getRawTransportDict()
	
	#VC: return values can be modified here
	return None


#################################
# Tool Code
#################################

def initTools(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawTool = vizconnect.getRawToolDict()
	
	#VC: return values can be modified here
	return None


#################################
# Avatar Code
#################################

def initAvatars(initFlag=vizconnect.INIT_INDEPENDENT, initList=None):
	#VC: place any general initialization code here
	rawAvatar = vizconnect.getRawAvatarDict()
	
	#VC: return values can be modified here
	return None


#################################
# Application Settings
#################################

def initSettings():
	#VC: apply general application settings
	viz.mouse.setTrap(False)
	viz.mouse.setVisible(viz.MOUSE_AUTO_HIDE)
	vizconnect.setMouseTrapToggleKey('')

	#VC: return values can be modified here
	return None


#################################
# Post-initialization Code
#################################

def postInit():
	"""Add any code here which should be called after all of the initialization of this configuration is complete.
	Returned values can be obtained by calling getPostInitResult for this file's vizconnect.Configuration instance."""
	return None


#################################
# Stand alone configuration
#################################

def initInterface():
	#VC: start the interface
	vizconnect.interface.go(__file__,
							live=True,
							openBrowserWindow=True,
							startingInterface=vizconnect.interface.INTERFACE_ADVANCED)

	#VC: return values can be modified here
	return None


###############################################

if __name__ == "__main__":
	initInterface()
	viz.add('piazza.osgb')
	viz.add('piazza_animations.osgb')

