import subprocess
import logging 

def toggle_fan(state):
    command = f"sudo uhubctl -l 1-1 -p 2 -a {state}"
    try:
        subprocess.run(command, shell=True)
    except Exception as e:
        logging.error(f"Error: {e}")
        
        