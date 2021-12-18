import time
import serial
import paho.mqtt.client as pc
from paho.mqtt import subscribe as sub

broker = "broker.hivemq.com"
sub_to = "house/bulb1"
plate = serial.Serial('COM7', timeout=1)

current = 0
state = False

def msg_print(client, data, msg):
    global current
    global state
    
    print(time.time(), ": ", msg.payload.decode('utf-8'), sep="")
    if (not(msg.payload.decode('utf-8').isdigit())):
        if (current < 250):
            plate.write(b'z')
        elif (current < 350):
            plate.write(b'x')
        else:
            plate.write(b'c')
        state = True
    else:
        if (state):
            state = False
            current = 0
        val = int(msg.payload.decode('utf-8'))
        current = current * 10 + val


plate.write(b'z')
print("HEY, LISTEN!")
sub.callback(msg_print, sub_to, hostname=broker)
