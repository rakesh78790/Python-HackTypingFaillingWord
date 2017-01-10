import cv2
from image_utils import take_screenshot


drawing = False  # true if mouse is pressed
ref_points = {}


def draw_rect(event, x, y, flags, param):
    global ref_points, drawing, original_image, cloned_image

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ref_points = {'lefttop': (x, y), }
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cloned_image = original_image.copy()
            cv2.rectangle(cloned_image, ref_points['lefttop'],
                          (x, y), (0, 255, 0), 1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cloned_image = original_image.copy()
        ref_points['rightbottom'] = (x, y)
        cv2.rectangle(cloned_image, ref_points['lefttop'],
                      ref_points['rightbottom'], (0, 255, 0), 1)


def create_region(image):
    global original_image, cloned_image, ref_points

    original_image = image
    cloned_image = image.copy()

    cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
    cv2.moveWindow("image", 0, 0)
    cv2.setWindowProperty(
        "image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback('image', draw_rect)

    while(1):
        cv2.imshow('image', cloned_image)
        k = cv2.waitKey(1) & 0xFF
        # print(k)
        if k == 27:  # esc
            ref_points = {}
            break
        elif k == 13:  # enter
            break
    cv2.destroyAllWindows()

    return ref_points


def specify_image_bbox():
    screenshot = take_screenshot()
    ref_points = create_region(screenshot)
    bbox = None
    if ref_points:
        bbox = (ref_points['lefttop'][0], ref_points['lefttop'][
                  1], ref_points['rightbottom'][0], ref_points['rightbottom'][1])
    return bbox
