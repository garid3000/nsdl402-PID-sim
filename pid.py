import numpy as np
import time

#last = 0

def readFloat(fname, last):
	#global last
	try:
		file = open(fname, 'r')
		val = float(file.read())
		file.close()
		#last = val
		return val
	except:
		return last

def writeFloat(fname, val):
	file = open(fname, 'w')
	file.write("{:.3f}".format(val))
	file.close()

sensor = 0
desire = 0
while 1:
	sensor = readFloat("motor.txt", sensor)
	desire = readFloat("desired.txt", desire)
	delta = desire - sensor
	writeFloat("torque.txt", delta*0.1)

