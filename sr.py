# mainly sourced from http://trac.srobo.org/wiki/RobotAPI
# and https://www.studentrobotics.org/docs/programming/

# Constants
vision = RED = BLUE = GREEN = 13

# Coroutinens

def add_coroutine(func, *args, **keys):
	pass

def coroutine(func):
	pass

# Motor

motor = []

# JointIO

io = []

# Query

class query():
	io = []
	vision = None

	class power():
		def beep_queue(self):	# n
			pass

	def timeout(self):	# time
		pass

# PWM

pwm = [0,1,2,3,4,5,6,7]

# Power

class power():
	led = [0,1,2,3,4,5,6,7]

	def beep(self, time=1):	# hz, time
		pass

# Logic Expressions

def And(*args):
	pass
