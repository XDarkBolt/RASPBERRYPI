from gpiozero import LED, Button
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
led = LED(24)
button = Button(23)
while True:
    

    button.when_pressed = led.on
    button.when_released = led.off
