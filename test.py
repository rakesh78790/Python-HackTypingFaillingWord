from specify_bound_box import specify_image_bbox
from extract_text_from_a_region import extract_text_from_a_region, send_keyboard_event


def test1():
    bbox = specify_image_bbox()
    text_filepath = extract_text_from_a_region(bbox)
    send_keyboard_event(text_filepath)


test1()
