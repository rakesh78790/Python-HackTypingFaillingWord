
import cv2
from subprocess import call
from image_utils import take_screenshot


def make_image_blackwhite(image):
    cv2.imshow('Image', image)
    cv2.waitKey(0)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]

    cv2.imshow('Image', thresh)
    cv2.waitKey(0)

    return thresh


def extract_text_from_image(image):
    # Save image to file
    input = './screenshot.png'
    cv2.imwrite(input, image)

    # Call Tesseract command line
    output = 'result'
    call(["tesseract", input, output])

    return './result.txt'


def extract_text_from_a_region(bbox=None):
    screenshot = take_screenshot(bbox)
    print('Take screenshot from bbox done')

    image = make_image_blackwhite(screenshot)
    print('Make image black and white done')

    text_filepath = extract_text_from_image(image)
    print('Extract text from image done')

    return text_filepath



