import cv2
from PIL import ImageGrab
import numpy


def take_screenshot(bbox=None):
    if bbox is None:
        pil_image = ImageGrab.grab()
    else:
        pil_image = ImageGrab.grab(bbox=bbox)

    opencv_image = cv2.cvtColor(numpy.array(pil_image), cv2.COLOR_RGB2BGR)
    return opencv_image
