from vpython import *
import time
import numpy as np
#obj = box(pos = vector(0,10,0), size = vector(10,1,10))
obj1 = box(pos = vector(0, 5,0), size = vector(  9, .1,  9))
obj2 = box(pos = vector(0,-5,0), size = vector(  9, .1,  9))
obj3 = box(pos = vector( 5,0,0), size = vector( .1,  9,  9))
obj4 = box(pos = vector(-5,0,0), size = vector( .1,  9,  9))
obj5 = box(pos = vector(0,0, 5), size = vector(  9,  9, .1))
obj6 = box(pos = vector(0,0,-5), size = vector(  9,  9, .1))
cyl  = cylinder(pos=vector(0,0,-1), axis=vector(0,0,2), radius=3, texture={'file':textures.metal, 'place':'right'} )



#obj3 = box(pos = vector(0,10,0), size = vector(  9, .1,  9))
#obj4 = box(pos = vector(0,10,0), size = vector(  9, .1,  9))
satObjs = [obj1, obj2, obj3, obj4, obj5, obj6]
axisArrowX = arrow(pos = vector(0,0,0), axis = vector(15,0,0), shaftwidth = .1, color = vector(1,0,0))
axisArrowY = arrow(pos = vector(0,0,0), axis = vector(0,15,0), shaftwidth = .1, color = vector(0,1,0))
axisArrowZ = arrow(pos = vector(0,0,0), axis = vector(0,0,15), shaftwidth = .1, color = vector(0,0,1))

ang = 0
while 1:
	for obj in satObjs:
		obj.rotate(angle = .1*np.pi/180,  axis=vec(0,0,1), origin=vector(0,0,1000))
	cyl.rotate(angle = -.2*np.pi/180, axis=vec(0,0,1), origin=vector(0,0,1000))
	time.sleep(0.01)
	ang += 1
	print(ang)
