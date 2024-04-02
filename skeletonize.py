import cv2 as cv
import numpy as np

def spookyScary(frame):
    # Threshold for monotone

    ret, frame = cv.threshold(frame, 127, 255, cv.THRESH_BINARY)

    # Create empty skeleton
    size = np.size(frame)
    skele = np.zeros(frame.shape, np.uint8)

    # Get cross shaped kernel
    element = cv.getStructuringElement(cv.MORPH_CROSS, (3,3))

    while True:
        # Open frame
        open = cv.morphologyEx(frame, cv.MORPH_OPEN, element)

        # Subtract open from frame
        tempFrame = cv.subtract(frame, open)

        # Erode and refine
        erodeFrame = cv.erode(frame, element)
        skele = cv.bitwise_or(skele, tempFrame)
        lame = erodeFrame.copy()

        try:
            if cv.countNonZero(frame) == 0:
                break

        except: pass

        return [skele, frame]

