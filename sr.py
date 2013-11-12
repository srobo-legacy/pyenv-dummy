'''
This is a dummy implementation of the SR API, as documented at:
* http://trac.srobo.org/wiki/RobotAPI
* http://srobo.org/docs/programming/
This should not be considered canonical!
'''

# Imports
from collections import namedtuple as _namedtuple

# Constants
MARKER_ARENA = 13
MARKER_ROBOT = 13
MARKER_SLOT = 13
MARKER_TOKEN_TOP = 13
MARKER_TOKEN_BOTTOM = 13
MARKER_TOKEN_SIDE = 13

INPUT = "INPUT"
OUTPUT = "OUTPUT"
INPUT_PULLUP = "INPUT_PULLUP"

# Power

class Battery:
    def __init__(self):
        self.voltage = 12.3
        self.current = 1.3

class Power:
    def __init__(self):
        self.led = [0,1,2,3,4,5,6,7]
        self.battery = Battery()

    def beep(self, hz, time=1):
        pass

# Motor

class Motor(object):
    def __init__(self):
        MotorChannel = _namedtuple( "MotorChannel", "power" )

        self.m0 = MotorChannel()
        self.m1 = MotorChannel()

# Ruggeduino

class Ruggeduino(object):
    def pin_mode(self, pin, mode):
        pass

    def digital_read(self, pin):
        return False

    def digital_write(self, pin, value):
        pass

    def analogue_read(self, pin):
        return False

# Vision

MarkerInfo = _namedtuple( "MarkerInfo", "code marker_type offset size" )
ImageCoord = _namedtuple( "ImageCoord", "x y" )
WorldCoord = _namedtuple( "WorldCoord", "x y z" )
PolarCoord = _namedtuple( "PolarCoord", "length rot_x rot_y" )
Orientation = _namedtuple( "Orientation", "rot_x rot_y rot_z" )
Point = _namedtuple( "Point", "image world polar" )

class Marker:
    def __init__(self):
        # Aliases
        self.info = MarkerInfo()
        self.timestamp = 3.14159
        self.res = (800, 600)
        self.vertices = []
        self.centre = Point()
        self.dist = 42
        self.rot_y = 13
        self.orientation = Orientation()

# Logic Expressions

def And(*args):
    return args

def Or(*args):
    return args

# Robot

class Robot:
    @classmethod
    def setup(cls):
        return Robot()

    def __init__(self):
        self.usbkey = None
        self.startfifo = None
        self.mode = None
        self.zone = None
        self.motors = [Motor()]
        self.ruggeduinos = [Ruggeduino()]
        self.power = Power()
        self.servos = []

    def see(self, res = (800, 600), stats = False):
        """
        Make the robot see stuff
        """
        return [Marker()]

    def init(self):
        pass

    def wait_start(self):
        pass

    def ruggeduino_set_handler_by_id(self, r_id, handler):
        self.ruggeduinos = [handler()]

    def ruggeduino_set_handler_by_fwver(self, fwver, handler):
        self.ruggeduinos = [handler()]

    def ruggeduino_ignore_id( self, r_id ):
        "Ignore the Ruggeduino with the given ID"
        IgnoredRuggeduino = _namedtuple( "IgnoredRuggeduino", "path" )
        self.ruggeduino_set_handler_by_id(r_id, IgnoredRuggeduino)
