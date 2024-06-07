import Adafruit_DHT
import time

# Define the sensor type and the GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 16


def read_dht11():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        print(f"Temperature: {temperature:.1f}C, Humidity: {humidity:.1f}%")
    else:
        print("Failed to retrieve data from humidity sensor")


if __name__ == "__main__":
    try:
        while True:
            read_dht11()
            time.sleep(2)  # Read data every 2 seconds
    except KeyboardInterrupt:
        print("Program terminated")