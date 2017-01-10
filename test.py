from specify_bound_box import specify_image_bbox
from extract_text_from_a_region import extract_text_from_a_region
from keyboard_utils import send_keys_from_file


def test1():
    bbox = specify_image_bbox()
    text_filepath = extract_text_from_a_region(bbox)
    send_keys_from_file(text_filepath)


test1()
