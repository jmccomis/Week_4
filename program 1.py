from gpiozero import LED,Button
from signal import pause

led= LED(18)
button= Button(26)
button.when_pressed = led.blink
button.when_released = led.off

pause()