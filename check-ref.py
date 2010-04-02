from sr import *

def cheese():
    while True:
        yield 1
        print "I'm a Robot"

@coroutine
def cheese2():
    while True:
        print "I can tell you I'm a robot before main adds me!"
        yield 1


def main():

    add_coroutine(cheese)

    yield 3.4 #waits 3.4 seconds

    yield 5
    if event == timeout:
        # timeout occurred
        print "BANG"


#MOTOR
    ########## Configuring the motor controller
    #### Sensors:
    # Null sensor: this is the default.
    motor[0].sensor = motor.NULL
    # Use AS5030 on channel 0
    motor[0].sensor = motor.AS5030

    # Select which feedback pins are connected to which pin:
    motor[0].as5030.set_pins( clk = 0, dio = 1 )
    # How many LSB's to discard from sensor (default:0)
    motor[0].as5030.set_shr( 2 )

    #### Controllers:
    ## Selecting the controller:
    # Unity (multiply target by 1): this is the default
    motor[0].controller = motor.UNITY
    # Use PID control on this channel:
    motor[0].controller = motor.PID

    ## Configuring the PID controller:
    motor[0].PID.set_coeff( kp = -4, ki = -5, kd = -10 )
    # Which can also be called like this:
    motor[0].PID.sef_coeff(-4,-5,-10)

    # Enable a channel:
    motor[0].enable()
    # Disable a channel:
    motor[0].disable()

    ########## Operating the motor controller:

    # Set the target
    # When using unity controller, this must be in [-100,100]
    motor[0].target = 30
    motor[0].target = -90
    # When using PID controller, can be any 32-bit signed int, e.g:
    motor[0].target = 3049
    motor[0].target = -23

    # motor[0].target and motor[1].target can also be used to find the current target.

    # Wait for the motor to reach its target
    # (obviously only valid when a sensor + controller is in use):
    yield motor[0]

    #get feedback position
    motor[0].getpos()


#JOINTIO
    # Read the digital value of pin 3:
    foo = io.pin[3]
    # Or:
    foo = readpin(3)

    # Read the analogue reading from pin 3
    jam = io.apin[3]
    # Or:
    jam = readapin(3)

    # Set output 1 high:
    io.pin[1] = 1
    # Or:
    setoutput(1,1)

#EVENTS
    # Wait for input 3 to change digital value
    yield io.pin[3]

    # Wait for input 3 to become digital '1' (threshold 512)
    yield io.pin[3] == 1

    # Wait for input 3 readings to exceed 1V
    yield io.apin[1] > 1

    # Wait for input 2 readings to go below 2.5V
    yield io.apin[2] < 2.5

    # The analogue pins do not have the "==" operator.

#LOGIC
    # OR:
    yield io.pin[3] == 1, io.pin[2] == 0
    yield io.apin[3] > 2, io.apin[3] < 3

    # AND:
    yield (io.pin[3] == 1) & (io.pin[2] == 0)
    # alternatively:
    yield And( io.pin[3] == 1, io.pin[2] == 0 )

    if event == io:
        pass

    yield io.apin[1] > 1.6, (io.pin[2] == 1) & (io.pin[3] == 0)
    if 2 in event.io.pins:
        # event.io.vals is an array of the pin values
        # e.g. event.io.vals[2] gives the value of the pin when the event happened
        # the value of event.io.vals[0] is meaningless
        # (and may later throw an error if read at the wrong time)
        pass
    elif 1 in event.io.pins:
        # event.io.vals[1] is a voltage (float)
        pass

#PWM
    # set servo SERVO_NUMBER to position 0.0 <= POS <= 100.0
    setpos(1, 1)

    # read servo position - returns servo position
    foo = readpos(1)

    # Also accessible through:
    pwm[1] = 1
    # This can also be read:
    foo = pwm[1]

    # Set screen 0 to read "badgers and jam"
    lcd[0] = "badgers and jam"

    # or if that's too annoying to implement in the time:
    setlcd(0, "badgers and jam")

#POWER
    #similar to jio inputs...
    if power.switch[0] == 1:
        pass

    #and similar to jio outputs
    power.led[0] = 1
    #or
    setled(0,1)

    #similarly
    bees = getled(1)

    yield 2
    if event == power_switch:
        #event.power_switch.switches is a list of switches that changed
        #event.power_switch.vals is like event.io.vals
        pass

#VISION
    #wait for vision event
    yield vision()

    if event == vision:
        for blob in event.vision.blobs:
            # blob has the following properties:
            # .x (was centrex)
            # .y (was centrey)
            # .mass
            # .colour (RED, BLUE, YELLOW, GREEN, ...)
            # .height
            # .width
            # VISION_HEIGHT and VISION_WIDTH are the size of the image in pixels
            pass
        myblob = event.vision.blobs[0]
        print myblob.x, myblob.y, myblob.mass, myblob.colour, myblob.height, myblob.width
