'''
This is a dummy implementation of the SR API, as documented at:
* http://trac.srobo.org/wiki/RobotAPI
* http://srobo.org/docs/programming/
This should not be considered canonical!
'''

# Constants
vision = RED = BLUE = GREEN = 13

# Power

class Power():
    led = [0,1,2,3,4,5,6,7]

    def beep(self, hz, time=1):
        pass

# Logic Expressions

def And(*args):
    return args

# TODO: check that Or doesn't exist

# Robot

class Robot:
    usbkey = None
    startfifo = None
    mode = None
    zone = None
    motor = []
    io = []
    power = Power()
    servo = []

def see(resolution = (800, 600)):
	return []

def wait_for(*args):
	return args
