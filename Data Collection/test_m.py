import csv
import datetime
from pynput import keyboard

stop_listener = False
key_press_times = {}  # Dictionary to store press times

with open('D:\\user_authentication\\test_m.csv', 'a+', newline='') as csvfile:
    fieldnames = ['event', 'key', 'time', 'duration', 'backspace_used']
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

        # Check if the backspace key is pressed
        backspace_used = 1 if key == keyboard.Key.backspace else 0
        
        # Print the character to the console
        if key == keyboard.Key.backspace:
            print('\b \b', end='', flush=True)  # Simulate backspace effect
        elif key == keyboard.Key.enter:
            print('\n', end='', flush=True)
        elif key == keyboard.Key.space:
            print(' ', end='', flush=True)
        elif hasattr(key, 'char') and key.char is not None:
            print(key.char, end='', flush=True)
        else:
            print(f'[{key}]', end='', flush=True)

        writer.writerow({'event': 'press', 'key': key_char, 'time': press_time, 'duration': '', 'backspace_used': backspace_used})
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
        
        # Record backspace usage only for the press event
        backspace_used = 1 if key == keyboard.Key.backspace else 0

        writer.writerow({'event': 'release', 'key': key_char, 'time': release_time, 'duration': duration, 'backspace_used': backspace_used})
        csvfile.flush()
        
        if key == keyboard.Key.esc:
            stop_listener = True
            return False

    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    while not stop_listener:
        pass

print("Listener stopped")
