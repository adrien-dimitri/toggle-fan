from dotenv import load_dotenv
from get_temperature import get_temperature
from toggle_fan import toggle_fan

import time
import os
import logging

load_dotenv()

lat = os.getenv('LAT')
lon = os.getenv('LON')
api_key = os.getenv('API_KEY')

logging.basicConfig(filename='logs.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

while True:
    temp = get_temperature(lat, lon, api_key)

    if temp is not None:
        if temp > 20:
            toggle_fan(1)
            logging.info('ON')
        else:
            logging.info('OFF')
            toggle_fan(0)
    
    logging.info(f'CURRENT TEMP: {temp}') 
    time.sleep(300)
