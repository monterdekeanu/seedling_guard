import Adafruit_DHT
import time
import tkinter as tk

# Define the sensor type and the GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4


class DHT11App:
    def __init__(self, root):
        self.root = root
        self.root.title("DHT11 Temperature and Humidity Sensor")

        self.temperature_label = tk.Label(root, text="Temperature: ", font=("Helvetica", 16))
        self.temperature_label.pack(pady=10)

        self.humidity_label = tk.Label(root, text="Humidity: ", font=("Helvetica", 16))
        self.humidity_label.pack(pady=10)

        self.update_readings()

    def update_readings(self):
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            self.temperature_label.config(text=f"Temperature: {temperature:.1f}°C")
            self.humidity_label.config(text=f"Humidity: {humidity:.1f}%")
        else:
            self.temperature_label.config(text="Failed to retrieve data from humidity sensor")
            self.humidity_label.config(text="")

        self.root.after(2000, self.update_readings)  # Update the readings every 2 seconds


if __name__ == "__main__":
    root = tk.Tk()
    app = DHT11App(root)
    root.mainloop()
