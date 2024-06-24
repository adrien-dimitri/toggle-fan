from get_temperature import get_temperature
from toggle_fan import toggle_fan
import time


while True:
    temp = get_temperature()
    
    if temp is not None:
        if temp > 30:
            toggle_fan('on')
        else:
            toggle_fan('off')
    
    time.sleep(300)