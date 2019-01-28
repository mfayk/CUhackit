# import the dragonboard GPIO
#import "" as GPIO

import mraa
import time

def buzzer (distance,beeps, pin):
    buzzer = mraa.Gpio(pin)
    buzzer.dir(mraa.DIR_OUT)
    for i in range(beeps):
        time.sleep(.1-5*distance)
        buzzer.write(1)
        time.sleep(distance)
        buzzer.write(0)

#print(mraa.getVersion())

TRIG = mraa.Gpio(29)
ECHO = mraa.Gpio(30)


while (1):

    TRIG.dir(mraa.DIR_OUT)
    ECHO.dir(mraa.DIR_IN)

    TRIG.write(0)
    time.sleep(0.25)
    TRIG.write(1)


    time.sleep(0.00001)

    TRIG.write(0)

    while ECHO.read() == 0:
        pulse_start = time.time()

    while ECHO.read() == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start;

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    print "Distance:",distance, "cm"
    if (distance <= 90):
        #buzzer(distance/10000,3,31)
        print("beep")
