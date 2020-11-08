from pynput import keyboard
globalKey=None



def on_press(key):
    global globalKey
    try:
        print(key.char.replace("'", ""))
        globalKey=key.char.replace("'", "")
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    global globalKey
    globalKey=None
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
""" with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join() """

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()




def main(key):
    lastKey=key
    string=""
    while True:
        global globalKey

        if lastKey!=globalKey:
            if globalKey!=None:
                string=string+globalKey
                print(string)
        
        lastKey=globalKey

main(globalKey)