'''
This is a dummy student code file, which attempts to use as much of the
SR API as it can, in as many ways as is sane and some that aren't.
This should not be considered a reference for the API, instead you should
read the docs (http://srobo.org/docs/programming), or see the trac page
about the API: http://srobo.org/trac/wiki/RobotAPI.
'''

from __future__ import print_function

import sr.robot
from sr.robot import *

import os

R = sr.robot.Robot()

print(R.usbkey)
print("usb path is :" + R.usbkey)
print(R.startfifo)
print(R.mode)
print("mode is :" + R.mode)
print(R.zone)
mylist = ['a', 'b']
print(mylist[R.zone])
print("zone is :%d" % (R.zone,))

a_file = os.path.join(R.usbkey, "my-file.txt")

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
    first.m0.power = 19

    # In a loop
    for m in R.motors.values():
        l = m.m0
        r = m.m1
        print(l.power)
        l.power = 42
        print(r.power)
        r.power = 21

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

    print("Common marker types: ", MARKER_ARENA, MARKER_ROBOT)
    print("Game marker types: ", MARKER_TOKEN_A, MARKER_TOKEN_B, MARKER_TOKEN_C)

    for marker in markers:
        print(marker)
        print(marker.info)
        print(marker.info.code)
        print(marker.info.marker_type)
        print(marker.info.token_net)
        print(marker.info.offset)
        print(marker.info.size)
        print(marker.timestamp)
        print(marker.res)
        print(marker.res[0])
        print(marker.res[1])
        print(marker.vertices)
        print(len(marker.vertices))
        print(marker.vertices[0])
        print(marker.centre)
        print(marker.centre.image)
        print(marker.centre.image.x)
        print(marker.centre.image.y)
        print(marker.centre.world)
        print(marker.centre.world.x)
        print(marker.centre.world.y)
        print(marker.centre.world.z)
        print(marker.centre.polar)
        print(marker.centre.polar.length)
        print(marker.centre.polar.rot_x)
        print(marker.centre.polar.rot_y)
        print(marker.dist)
        print(marker.rot_y)
        print(marker.orientation)
        print(marker.orientation.rot_x)
        print(marker.orientation.rot_y)
        print(marker.orientation.rot_z)

def ruggeduino_things():
    '''
    Explore ruggeduinos
    '''

    # to set Ruggeduino board 0's pin 2 to output
    R.ruggeduinos[0].pin_mode(2, OUTPUT)
    # to set Ruggeduino board 0's pin 3 to input
    R.ruggeduinos[0].pin_mode(3, INPUT)
    R.ruggeduinos[0].pin_mode(3, INPUT_PULLUP)

    # to read Ruggeduino board 0's digital pin 3...
    pin0 = R.ruggeduinos[0].digital_read(3)

    print(pin0)

    # to read Ruggeduino board 0's analogue pin A0...
    pin0 = R.ruggeduinos[0].analogue_read(0)

    print(pin0)

    # to set Ruggeduino board 0's pin 2 high:
    R.ruggeduinos[0].digital_write(2, True)

    # to set Ruggeduino board 0's pin 2 low:
    R.ruggeduinos[0].digital_write(2, False)

    # Access Ruggeduino by id
    first = R.ruggeduinos["sr01234"]
    first.digital_write(3, False)

    # In a loop
    for duino in R.ruggeduinos.values():
        duino.pin_mode(3, INPUT)
        print(duino.digital_read(3))
        duino.digital_write(0, False)
        print(duino.analogue_read(0))

def power_things():
    '''
    Explore power things
    '''

    print(R.power.battery.voltage, R.power.battery.current)
    R.power.beep(500, note='d')
    R.power.beep(2000, frequency=400)

    R.power.output[0] = False
    R.power.output[0] = True

    R.power.output[OUT_H0] = True
    R.power.output[OUT_H1] = True
    R.power.output[OUT_L0] = True
    R.power.output[OUT_L1] = True
    R.power.output[OUT_L2] = True
    R.power.output[OUT_L3] = True

    # Not yet supported
    is_on = R.power.output[0]
    for x in R.power.output:
        pass

def servo_things():

    # servo[N][SERVO_NUMBER] = POS

    # set servo 1's position (on PWM board 0) to 50.0
    R.servos[0][1] = 50.0

    first = R.servos[0]
    first[1] = 49
    print(first[1])

    more = R.servos["ABC"]
    more[2] = 49
    print(more[2])

    # variable = pwm[N][SERVO_NUMBER]

    # store the position of PWM board 0's servo 0 in 'bees'
    bees = R.servos[0][0]
    print(bees)

    for sb in R.servos:
        sb[1] = 49
        print(sb[1])

class CustomRuggeduino(Ruggeduino):
    def test(self):
        print("test")

    # function for instructing a Ruggeduino to bake a cake
    def bake_cake(self):
        with self.lock:
            self.command("c")

    # function for instructing a Ruggeduino to bake another cake
    def bake_cake2(self):
        with self.lock:
            resp = self.command("c")
        return int(resp)

def alt_duino_things():
    # a) Using the ruggeduino ID:
    R = Robot.setup()
    R.ruggeduino_set_handler_by_id( "123123123123123", CustomRuggeduino )
    R.init()
    R.wait_start()
    R.ruggeduinos[0].test()

    # b) Using the first part of the firmware version:
    R = Robot.setup()
    R.ruggeduino_set_handler_by_fwver( "SRcustom", CustomRuggeduino )
    R.init()
    R.wait_start()
    R.ruggeduinos[0].test()

    R.ruggeduinos[0].bake_cake()
    print(R.ruggeduinos[0].bake_cake2())
    # and you'll still be able to do this:
    R.ruggeduinos[0].digital_read(3)

    # 3) Use their own firmware not based on our firmware
    R = Robot.setup()
    R.ruggeduino_ignore_id( "123123123123123" )
    R.init()

    # This is the ignored ruggeduino's device path
    print(R.ruggeduinos[0].path)

    R.wait_start()

    # this will error, unfortunately
    #for r in R.ruggeduinos:
    #    r.path
    #    r.serialnum
    #    r.test()

if __name__ == '__main__':
    motor_things()
    power_things()
    ruggeduino_things()
    servo_things()
    vision_things()
    alt_duino_things()
