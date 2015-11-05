'''
This is a dummy implementation of the SR API, as documented at:
* http://trac.srobo.org/wiki/RobotAPI
* http://srobo.org/docs/programming/
This should not be considered canonical!
'''

# Imports
from collections import namedtuple as _namedtuple

# Constants
MARKER_ARENA, MARKER_ROBOT = 'arena', 'robot'
MARKER_TOKEN_TOP, MARKER_TOKEN_SIDE, MARKER_TOKEN_BOTTOM = 'top', 'side', 'bottom'
NET_A, NET_B, NET_C = 'a', 'b', 'c'

INPUT = "INPUT"
OUTPUT = "OUTPUT"
INPUT_PULLUP = "INPUT_PULLUP"

# Power

class Battery(object):
    def __init__(self):
        self.voltage = 12.3
        self.current = 1.3

class Power(object):
    def __init__(self):
        self.battery = Battery()

    def beep(self, duration, note=None, frequency=None):
        pass

# Motor

class Motor(object):
    def __init__(self):
        class MotorChannel(object):
            def __init__(self):
                self.power = 0

        self.m0 = MotorChannel()
        self.m1 = MotorChannel()

# Ruggeduino

class Ruggeduino(object):
    # Custom Ruggeduino things
    lock = None

    def command(self, string):
        pass

    # Plain Ruggeduino things
    def pin_mode(self, pin, mode):
        pass

    def digital_read(self, pin):
        return False

    def digital_write(self, pin, value):
        pass

    def analogue_read(self, pin):
        return False

# Vision

MarkerInfo = _namedtuple( "MarkerInfo", "code marker_type token_net offset size" )
ImageCoord = _namedtuple( "ImageCoord", "x y" )
WorldCoord = _namedtuple( "WorldCoord", "x y z" )
PolarCoord = _namedtuple( "PolarCoord", "length rot_x rot_y" )
Orientation = _namedtuple( "Orientation", "rot_x rot_y rot_z" )
Point = _namedtuple( "Point", "image world polar" )

class Marker(object):
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

# Robot

class Robot(object):
    @classmethod
    def setup(cls):
        return Robot()

    def __init__(self):
        self.usbkey = None
        self.startfifo = None
        self.mode = None
        self.zone = None
        self.motors = {0: Motor()}
        self.ruggeduinos = {0: Ruggeduino()}
        self.power = Power()
        self.servos = {0: []}

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
        IgnoredRuggeduino = _namedtuple( "IgnoredRuggeduino", "path serialnum" )
        self.ruggeduino_set_handler_by_id(r_id, IgnoredRuggeduino)
