# Save on CPX/CPB as code.py
# Blinks the top right RED LED
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    print("hello")
    while True:
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)

main()