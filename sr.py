# mainly sourced from http://trac.srobo.org/wiki/RobotAPI

# Constants
motor = power_switch = timeout = RED = BLUE = GREEN = VISION_HEIGHT = VISION_WIDTH = 13

# Coroutinens

def add_coroutine(func):
	pass

def coroutine(func):
	pass

# Motor

class Motor():
	sensor = None
	controller = None
	target = None

	def enable(self):
		pass

	def disable(self):
		pass

	def getpos(self):
		pass

	class as5030():
		def set_pins( clk = 0, dio = 1 ):
			pass

		def set_shr( a ):
			pass

	class PID():
		def set_coeff( kp = -4, ki = -5, kd = -10 ):
			pass


class Motors(list):
	# Sensor types
	NULL = "null sensor"
	AS5030 = ADS5030 = "ads5030 sensor"

	# Controller types:
	UNITY = "unity controller"
	PID = "pid controller"

	def __init__(self):
		list.__init__(self)
		self.append( Motor() )
		self.append( Motor() )

motor = Motors()

# JointIO

# Read the digital value of a pin:
def readpin(a):
	pass

# Read the analogue reading from a pin:
def readapin(a):
	pass

# Set an output:
def setoutput(a,b):
	pass

class io():
	pin = [0,1,2,3,4,5,6,7]
	apin = [0,1,2,3,4,5,6,7]

# Event

class event():
	class io():
		pins = [0,1,2,3,4,5,6,7]
		apins = [0,1,2,3,4,5,6,7]

	class power_switch():
		switches = [0,1,2,3]
		vals = [0,1,2,3]

	class vision():
		class blob():
			x = y = mass = colour = height = width = 2
		blobs = []

# Logic ExpressionS

def Or(*args):
	pass

def And(*args):
	pass

# PWM

pwm = [0,1,2,3,4,5,6,7]

# set servo SERVO_NUMBER to position 0.0 <= POS <= 100.0
def setpos(n, pos):
	pass

# read servo position - returns servo position
def readpos(n):
	pass

def setlcd(n, msg=''):
	pass

lcd = [0,1,2,3]

# Power

def getled(a):
	pass

#similar to jio inputs...
def setled(a,b):
	pass

def setleds(a,b):
	pass

class power():
	led = [0,1,2,3,4,5,6,7]
	switch = [0,1,2,3]

# Vision

def vision():
	pass
