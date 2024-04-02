import cv2 as cv
import numpy as np
from perspectiveTransform import *
from laneDetection import *

def videoStreamProcess(port,p1,p2,p3,p4,cvThresh):
    # open video


    capture = cv.VideoCapture(port)

    while True:
        # capture frame
        ret, frame = capture.read()

        # establish trapezoid mask

        # if frame isn't read correctly, kill process
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        pts1 = np.float32([p1, p2, p3, p4])
        pts2 = np.float32([[0, 650], [0, 0], [400, 0], [400, 650]])

        # Apply Perspective Transform Algorithm
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        cFrame = cv2.warpPerspective(frame, matrix, (400, 650))

        cv.imshow('transfromers', cFrame)

        try:
            nallo, gallo, mallo = genesis(cFrame,cvThresh)
        except:
            pass

        procFrame = cv.cvtColor(cFrame, cv.COLOR_BGR2GRAY)

        pts = np.array([p1, p2, p3, p4],
                       np.int32)

        pts = pts.reshape((-1, 1, 2))

        isClosed = True

        # Blue color in BGR
        color = (255, 0, 0)

        # Line thickness of 2 px
        thickness = 2

        # Using cv2.polylines() method
        # Draw a Blue polygon with
        # thickness of 1 px
        image = cv2.polylines(frame, [pts],
                              isClosed, color, thickness)

        try:
            cv.imshow('lineDetect', nallo)
            cv.imshow('jahdfgl',gallo)
            cv.imshow('sakljfd',mallo)
        except:
            pass
        h, w = procFrame.shape

        cv.imshow('main', frame)
        cv.imshow('frame', cFrame)
        if cv.waitKey(1) == ord('q'):
            break

    capture.release()
    cv.destroyAllWindows()



