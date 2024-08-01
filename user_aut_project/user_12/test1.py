import csv
import datetime
from pynput import keyboard

stop_listener = False
key_press_times = {}  # Dictionary to store press times

with open('D:\\MLT assigments\\user_authentication\\user_12\\test1.csv', 'a+', newline='') as csvfile:
    fieldnames = ['event', 'key', 'time', 'duration']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    def on_press(key):
        global stop_listener
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        
        press_time = datetime.datetime.now()
        key_press_times[key_char] = press_time
        
        writer.writerow({'event': 'press', 'key': key_char, 'time': press_time, 'duration': ''})
        csvfile.flush()

    def on_release(key):
        global stop_listener
        try:
            key_char = key.char
        except AttributeError:
            key_char = str(key)
        
        release_time = datetime.datetime.now()
        
        press_time = key_press_times.pop(key_char, None)
        duration = (release_time - press_time).total_seconds() if press_time else ''
        
        writer.writerow({'event': 'release', 'key': key_char, 'time': release_time, 'duration': duration})
        csvfile.flush()
        
        if key == keyboard.Key.esc:
            stop_listener = True
            return False

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    while not stop_listener:
        pass

print("Listener stopped")
