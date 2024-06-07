import RPi.GPIO as GPIO
import time

# Setup
GPIO.setmode(GPIO.BCM)
input_pin = 16  # GPIO 16 (Physical pin 36)

GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    print("Connect a jumper wire between GPIO 16 (pin 36) and 3.3V (pin 1)")
    input("Press Enter to start the test...")

    for i in range(10):
        if GPIO.input(input_pin) == GPIO.HIGH:
            print("GPIO 16 is HIGH")
        else:
            print("GPIO 16 is LOW")
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
