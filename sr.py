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
    def __init__(self):
        self.led = [0,1,2,3,4,5,6,7]

    def beep(self, hz, time=1):
        pass

# Vision

MarkerInfo = namedtuple( "MarkerInfo", "code marker_type offset size" )
ImageCoord = namedtuple( "ImageCoord", "x y" )
WorldCoord = namedtuple( "WorldCoord", "x y z" )
PolarCoord = namedtuple( "PolarCoord", "length rot_x rot_y" )
Orientation = namedtuple( "Orientation", "rot_x rot_y rot_z" )
Point = namedtuple( "Point", "image world polar" )

# Logic Expressions

def And(*args):
    return args

def Or(*args):
    return args

# Robot

class Robot:
    def __init__(self):
        self.usbkey = None
        self.startfifo = None
        self.mode = None
        self.zone = None
        self.motors = []
        self.io = []
        self.power = Power()
        self.servo = []

    def see(self, res = (800, 600)):
        """
        Make the robot see stuff
        """
        return [Marker()]

def wait_for( *polls, **named ):
    """
    Wait for at least one of the passed polls to happen
    """
    import collections
    C = collections.namedtuple( "WaitResults", named.keys )
    return C( **named )
