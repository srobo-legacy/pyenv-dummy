'''
This is a dummy student code file, which attempts to use as much of the
SR API as it can, in as many ways as is sane and some that aren't.
This should not be considered a reference for the API, instead you should
read the docs (http://srobo.org/docs/programming), or see the trac page
about the API: http://srobo.org/trac/wiki/RobotAPI.
'''

import sr
from sr import *

R = sr.Robot()

print R.usbkey
print R.startfifo
print R.mode
print R.zone
print R.power.battery.voltage, R.power.battery.current

def motor_things():

    # motor 0, channel 0 to full power forward
    R.motors[0].m0.power = 100

    # motor 1, channel 0 to full power reverse
    R.motors[1].m0.power = -100

    # motor 0, channel 1 to half power forward
    R.motors[0].m1.power = 50

    # motor 1, channel 0 stopped
    R.motors[1].m0.power = 0

    # the following will put motor 0, channel 1 at 25% power (forwards) for 2.5 seconds:
    R.motors[0].m1.power = 25
    R.motors[0].m1.power = 0

    # get the current output power of motor 0, channel 0
    currentTarget = R.motors[0].m0.power

    # Access Motor by id
    first = R.motors["sr01234"]

def vision_things():
    '''
    Explore vision things
    '''

    # see what we can
    markers = R.see( res = (42, 19) )

    # see what we can
    markers = R.see( stats = True )

    # see what we can
    markers = R.see( res = (42, 19), stats = True )

    # see what we can
    markers = R.see()

    print "All marker types: ", MARKER_ARENA, MARKER_ROBOT, MARKER_SLOT, \
            MARKER_TOKEN_TOP, MARKER_TOKEN_BOTTOM, MARKER_TOKEN_SIDE

    for marker in markers:
        print marker
        print marker.info
        print marker.info.code
        print marker.info.marker_type
        print marker.info.offset
        print marker.info.size
        print marker.timestamp
        print marker.res
        print marker.res[0]
        print marker.res[1]
        print marker.vertices
        print len(marker.vertices)
        print marker.vertices[0]
        print marker.centre
        print marker.centre.image
        print marker.centre.image.x
        print marker.centre.image.y
        print marker.centre.world
        print marker.centre.world.x
        print marker.centre.world.y
        print marker.centre.world.z
        print marker.centre.polar
        print marker.centre.polar.length
        print marker.centre.polar.rot_x
        print marker.centre.polar.rot_y
        print marker.dist
        print marker.rot_y
        print marker.orientation
        print marker.orientation.rot_x
        print marker.orientation.rot_y
        print marker.orientation.rot_z

def ruggeduino_things():
    '''
    Explore ruggeduinos
    '''

    # stop the motor
    R.motors[0].target = 0

    # to set Ruggeduino board 0's pin 2 to output
    R.ruggeduinos[0].pin_mode(2, OUTPUT)
    # to set Ruggeduino board 0's pin 3 to input
    R.ruggeduinos[0].pin_mode(3, INPUT)
    R.ruggeduinos[0].pin_mode(3, INPUT_PULLUP)

    # to read Ruggeduino board 0's digital pin 3...
    pin0 = R.ruggeduinos[0].digital_read(3)

    print pin0

    # to read Ruggeduino board 0's analogue pin A0...
    pin0 = R.ruggeduinos[0].analogue_read(0)

    print pin0

    # to set Ruggeduino board 0's pin 2 high:
    R.ruggeduinos[0].digital_write(2, True)

    # to set Ruggeduino board 0's pin 2 low:
    R.ruggeduinos[0].digital_write(2, False)

    # Access Ruggeduino by id
    first = R.ruggeduinos["sr01234"]

def power_things():
    '''
    Explore power things
    '''

    # turn LED 0 on
    R.power.led[0] = 1       # WILL work
    R.power.led = 0          # WON'T WORK
    R.power[0].led[0] = 1    # WON'T WORK

    # to toggle LED 2, you can use
    R.power.led[2] = not R.power.led[2]

    R.power.beep(440, 0.5)

    # beep at 100Hz for 1s, then at 200Hz for 2s
    R.power.beep( [(100, 1), (200, 2)] )

    # ramp up from 100Hz to 1000Hz in 1s overall, with frequency jumps of 100Hz
    R.power.beep( [ (x*100, 0.1) for x in range(1, 10) ] )

    # servo[N][SERVO_NUMBER] = POS

    # set servo 1's position (on PWM board 0) to 50.0
    R.servos[0][1] = 50.0

    # variable = pwm[N][SERVO_NUMBER]

    # store the position of PWM board 0's servo 0 in 'bees'
    bees = R.servos[0][0]

    print bees

if __name__ == '__main__':
    motor_things()
    power_things()
    ruggeduino_things()
    vision_things()
