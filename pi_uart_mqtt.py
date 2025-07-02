
import serial
import paho.mqtt.client as mqtt

ser = serial.Serial('/dev/ttyUSB0', 9600)
mqtt_client = mqtt.Client()
mqtt_client.connect("localhost", 1883, 60)

while True:
    line = ser.readline().decode().strip()
    print("Received:", line)
    mqtt_client.publish("farm/sensors", line)
