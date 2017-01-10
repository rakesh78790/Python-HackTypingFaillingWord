from specify_bound_box import specify_image_bbox
from extract_text_from_image import extract_text_from_blackwhite_screen_region
from keyboard_utils import send_keys_from_file
import time
import keyboard

is_starting = False
bbox = None


def main():
    global bbox, is_starting
    time.sleep(0.5)

    # Specify bbox
    bbox = specify_image_bbox()
    if not bbox:
        print('You must specify a region')
        exit(0)
    print('bbox = ' + str(bbox))

    # Show guide
    register_hotkey()
    while not is_starting:
        print('Press Ctrl + Alt + Shift + K to start')
        print('Or Press Ctrl + Alt + Shift + L to stop')
        time.sleep(2)

    keyboard.record()


def handle_start_hotkey():
    global is_starting

    keyboard.remove_hotkey(start_hotkey)
    print('Start hacking')
    print('Press Ctrl + Alt + Shift + L to stop')

    is_starting = True

    while is_starting:
        text_filepath = extract_text_from_blackwhite_screen_region(bbox)
        send_keys_from_file(text_filepath)
        time.sleep(2)


def handle_stop_hotkey():
    global is_starting
    keyboard.remove_hotkey(start_hotkey)
    keyboard.remove_hotkey(stop_hotkey)
    print('Stop hacking')
    is_starting = False


def register_hotkey():
    global start_hotkey, stop_hotkey

    start_hotkey = keyboard.add_hotkey(
        'ctrl+alt+shift+k', handle_start_hotkey, blocking=True, timeout=2)
    stop_hotkey = keyboard.add_hotkey(
        'ctrl+alt+shift+l', handle_stop_hotkey, blocking=True, timeout=2)


main()
