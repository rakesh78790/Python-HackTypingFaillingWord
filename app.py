from specify_bound_box import specify_image_bbox
from extract_text_from_image import extract_text_from_blackwhite_screen_region
from keyboard_utils import send_keys_from_file
import time
import keyboard

is_starting = False
bbox = None


def main():
    global bbox, is_starting

    # Specify bbox
    bbox = specify_image_bbox()
    if not bbox:
        print('You must specify a region')
        exit(0)
    print('bbox = ' + str(bbox))

    # Show guide
    register_hotkey()
    print('Start listening to hotkey')
    print('Press Ctrl + Alt + Shift + K to start')
    print('Or Press ESC to stop listening to hotkey')

    keyboard.wait('esc')
    is_starting = False


def handle_start_hotkey():
    global is_starting, start_hotkey

    keyboard.remove_hotkey(start_hotkey)
    print('Start hacking')
    print('Press ESC to stop')

    is_starting = True

    while is_starting:
        text_filepath = extract_text_from_blackwhite_screen_region(bbox)
        send_keys_from_file(text_filepath)
        time.sleep(2)

    print('Stop hacking')


def register_hotkey():
    global start_hotkey

    start_hotkey = keyboard.add_hotkey(
        'ctrl+alt+shift+k', handle_start_hotkey, blocking=True, timeout=2)


main()
