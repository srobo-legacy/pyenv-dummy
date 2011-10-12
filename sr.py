'''
This is a dummy implementation of the SR API, as documented at:
* http://trac.srobo.org/wiki/RobotAPI
* http://srobo.org/docs/programming/
This should not be considered canonical!
'''

# Constants
MARKER_ARENA = MARKER_ROBOT = MARKER_TOKEN = MARKER_BUCKET_SIDE = MARKER_BUCKET_END = 13

# Power

class Power:
    led = [0,1,2,3,4,5,6,7]

    def beep(self, hz, time=1):
        pass

# Vision

class MarkerInfo:
    code = 42
    type = MARKER_ARENA
    offset = 0
    size = 1.23

# Logic Expressions

def And(*args):
    return args

def Or(*args):
    return args

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
    """
    Make the robot see stuff
    """
    return [MarkerInfo()]

def wait_for( *polls, **named ):
    """
    Wait for at least one of the passed polls to happen
    """
    import collections
    C = collections.namedtuple( "WaitResults", named.keys )
    return C( **named )
