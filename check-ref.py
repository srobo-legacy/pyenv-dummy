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

	yield query.io[4].input[1].d

	# Wait for digital input pin 3 on JointIO board 0 to change value
	yield query.io[0].input[3].d

	# Wait for digital input 3 on JointIO board 0 to become digital '1'
	yield query.io[0].input[3].d == 1

	# Wait for the reading of analogue input 3 on JointIO board 0 to exceed 1V
	yield query.io[0].input[1].a > 1

	# Wait for the reading of analogue input 2 on JointIO board 0 to drop below 2.5V
	yield query.io[0].input[2].a < 2.5


	# io[IO_BOARD_NUMBER].input[PIN_NO].d

	# to read JoinIO board 0's digital pin 0...
	pin0 = io[0].input[0].d

	# io[IO_BOARD_NUMBER].input[PIN_NO].a

	# to read JoinIO board 0's analogue pin 2...
	pin0 = io[0].input[2].a

	# io[IO_BOARD_NUMBER].output[PIN_NO].d = VALUE

	# to set JointIO board 0's pin 1 high:
	io[0].output[1].d = 1

	# to set JointIO board 0's pin 1 low:
	io[0].output[1].d = 0


	motor[0].target = 50   # WILL work, if motor 0 exists
	motor[1].target = -20  # WILL work, if motor 1 exists
	motor.target = 42      # WON'T WORK

	# the above is similar to the situation for 'io' and 'pwm'


	power.led[0] = 1       # WILL work
	power.led = 0          # WON'T WORK
	power[0].led[0] = 1    # WON'T WORK

	# the above is similar to the situation for 'vision'


	# turn LED 0 on
	power.led[0] = 1

	# turn LED 1 off
	power.led[1] = 0

	# to toggle LED 2, you can use
	power.led[2] = not power.led[2]

	power.beep(440, 0.5)

	# beep at 100Hz for 1s, then at 200Hz for 2s
	power.beep( [(100, 1), (200, 2)] )

	# ramp up from 100Hz to 1000Hz in 1s overall, with frequency jumps of 100Hz
	power.beep( [ (x*100, 0.1) for x in range(1, 10) ] )

	# wait until there is only 3 notes left in the beep queue
	yield query.power.beep_queue(3)


	# wait here for a vision event to occur, storing the event object
	ev = yield vision

	# check to see if the event was a vision event
	if ev.was(vision):

		# do something with all of the returned blobs
		# (print RED blob co-ords. in this case)
		for blob in ev.vision.blobs:

			if blob.colour == RED:
				print "Found red blob at " + str(blob.x) + ", " + str(blob.y)


