import cv2
import imutils

# Load image, grayscale, Gaussian blur, Otsu's threshold, dilate
def cards_from_image(path_to_image):
    img = cv2.imread(path_to_image)
    image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    original = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    dilate = cv2.dilate(thresh, kernel, iterations=1)

    # Find contours, obtain bounding box coordinates, and extract ROI
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda c: cv2.boundingRect(c)[0])
    #cnts = sorted(cnts, key = cv2.contourArea)
    image_number = 0
    for c in cnts:
        if cv2.contourArea(c) < 0:
            pause
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
        ROI = original[y:y + h, x:x + w]
        if (w > 680 and h > 800):
            cv2.imwrite("detectedCards/{}.png".format(image_number), ROI)
            image_number += 1

# cv2.imshow('image', image)
# cv2.imshow('thresh', thresh)
# cv2.imshow('dilate', dilate)
# cv2.waitKey()

cards_from_image("images/test.png")