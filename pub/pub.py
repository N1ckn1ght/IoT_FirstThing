import time
import paho.mqtt.client as paho
import serial


def get_data(ser, tries=3):
    for i in range(tries):
        data = ser.read().decode()
        print(data)
        if (data == ''):
            print("debug, warning: no data found on try:", (i + 1))
        else:
            break
    return data


broker = "broker.hivemq.com"
pub_to = "house/bulb1"
client = paho.Client("1")
ser = serial.Serial('COM4', timeout=1)

print("debug, connecting to:", broker)
client.connect(broker)
client.loop_start()
print("debug, publishing at:", pub_to)

while True:
    client.publish(pub_to, get_data(ser))
    time.sleep(0.1)

client.disconnect()
client.loop_stop()
