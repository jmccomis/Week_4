import Adafruit_DHT as dht
from time import sleep
from gpiozero import LED,Button
from signal import pause
import random

led= LED(18)
button= Button(26)
i=1
DHT = 4

while True:
    h,t = dht.read_retry(dht.DHT22, DHT)
    x=(t*9/5)+32
    if button.is_pressed:
        print(x), print("button was pushed")
    else:    
        print(x)
        sleep(5)
    
        
    
    