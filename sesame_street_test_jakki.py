﻿import viz
import vizact
import oculus

#####Turn Cluster Master Off in Vizard#####

room = viz.add('Z:\\VRITS 2014\\Jakki B\\Sesame Street Characters\\LABROOM.osgb')
room.emissive([1,1,1])
elmo = viz.add('Z:\\VRITS 2014\\Jakki B\\Sesame Street Characters\\Elmo\\elmo.cfg')
elmo.emissive([1,1,1])
elmo.setScale([2,2,2])
elmo.setPosition([-0.5,0,1])

grover = viz.add('Z:\\VRITS 2014\\Jakki B\\Sesame Street Characters\\Grover\\grover.cfg')
grover.emissive([1,1,1])
grover.setScale([2,2,2])
grover.setPosition([0.5,0,1.5])

viz.MainView.getHeadLight().disable()

hmd = oculus.Rift()

MOVE_SPEED = 2.0

def UpdateView():
  yaw,pitch,roll = hmd.getSensor().getEuler()
  m = viz.Matrix.euler(yaw,0,0)
  m.setPosition(viz.MainView.getPosition())
  dm = viz.getFrameElapsed() * MOVE_SPEED
  if viz.key.isDown(viz.KEY_UP):
    m.preTrans([0,0,dm])
  if viz.key.isDown(viz.KEY_DOWN):
    m.preTrans([0,0,-dm])
  if viz.key.isDown(viz.KEY_LEFT):
    m.preTrans([-dm,0,0])
  if viz.key.isDown(viz.KEY_RIGHT):
    m.preTrans([dm,0,0])
  m.setEuler([yaw,pitch,roll])
  viz.MainView.setMatrix(m)
  
vizact.ontimer(0,UpdateView)

vizact.onkeydown('r',hmd.getSensor().reset)

viz.setOption('viz.glFinish', 1)

viz.go(viz.FULLSCREEN)