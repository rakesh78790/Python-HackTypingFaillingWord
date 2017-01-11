from specify_bound_box import specify_image_bbox
from extract_text_from_image import extract_text_from_blackwhite_screen_region
from keyboard_utils import send_keys_from_file
import time
import keyboard
import threading


bbox = None


def main():
    global bbox,  start_hotkey

    # Specify bbox
    bbox = specify_image_bbox()
    if not bbox:
        print('You must specify a region')
        exit(0)
    print('bbox = ' + str(bbox))

    # Show guide
    start_hotkey = keyboard.add_hotkey('ctrl+alt+shift+k', handle_start_hotkey)
    print('Start listening to hotkey')
    print('Press Ctrl + Alt + Shift + K to start')
    print('Or Press ESC to stop listening to hotkey')

    keyboard.wait('esc')
    print('Hacking stop')


def start_hacking():
    print('Start hacking')
    print('Press ESC to stop')

    while True:
        text_filepath = extract_text_from_blackwhite_screen_region(bbox)
        send_keys_from_file(text_filepath)
        time.sleep(2)

    print('Finish stopping hacking')


def handle_start_hotkey():
    keyboard.remove_hotkey(start_hotkey)
    t = threading.Thread(target=start_hacking)
    t.start()


main()
