import csv
import datetime
from pynput import keyboard

stop_listener = False

with open('D:\\MLT assigments\\user_authentication\\user_12\\keystrokes.csv', 'a+', newline='') as csvfile:
    fieldnames = ['event', 'key', 'time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()  

    def on_press(key):
        global stop_listener
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        
        writer.writerow({'event': 'press', 'key': key_char, 'time': datetime.datetime.now()})
        csvfile.flush()  

    def on_release(key):
        global stop_listener
        key_char = str(key)
        
        writer.writerow({'event': 'release', 'key': key_char, 'time': datetime.datetime.now()})
        csvfile.flush()  
        
        if key == keyboard.Key.esc:
            stop_listener = True
            return False

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    while not stop_listener:
        pass

print("Listener stopped")
