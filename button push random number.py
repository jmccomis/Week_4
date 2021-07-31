from gpiozero import LED,Button
from signal import pause
import random
from time import sleep
led= LED(18)
button= Button(26)
i=1

while True:
    if button.is_pressed:
        x=random.randint(1,100)
        print(str(x) + ", button was pushed")
        
        sleep(.6)
    else:
        x=random.randint(1,100)
        print(str(x))
        sleep(5)
       
    
       
       
pause()       

              