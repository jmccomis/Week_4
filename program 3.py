import Adafruit_DHT as dht
from time import sleep
from gpiozero import LED,Button
from signal import pause
import random

led= LED(18)

DHT = 4

while True:
    h,t = dht.read_retry(dht.DHT22, DHT)
    x=(t*9/5)+32
    
    print(x)
    if x>70:
        led.on()
    else:
        led.off()
    sleep(5)