from pynput import keyboard
import time
import csv

keystrokes = []

def on_press(key):
    try:
        keystrokes.append((key.char, 'press', time.time()))
    except AttributeError:
        keystrokes.append((str(key), 'press', time.time()))

def on_release(key):
    keystrokes.append((str(key), 'release', time.time()))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

with open('D:\MLT assigments\user_authentication\user_12\keystrokes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Key", "Action", "Timestamp"])
    writer.writerows(keystrokes)
