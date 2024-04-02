import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from alg1 import *

def leftRight(lines,center):
    leftLines = []
    rightLines = []

    for line in lines:
        p1 = line[0]
        p2 = line[1]

        x1 = p1[0]
        x2 = p2[0]

        xAv = (x1+x2)/2

        if xAv < center:
            leftLines.append(line)

        else:
            rightLines.append(line)

    return leftLines, rightLines

def interpolate(lines):
    x = []
    y = []

    for line in lines:
        p1 = line[0]
        p2 = line[1]

        x1 = p1[0]
        y1 = p1[1]
        x2 = p2[0]
        y2 = p2[1]

        xAv, yAv = findCenterPoint(x1,y1,x2,y2)

        x.append(int(xAv))
        y.append(int(yAv))



    x = np.array(x)
    y = np.array(y)

    # Perform linear regression
    slope, intercept = np.polyfit(x, y, 1)

    # Generate x values for the line
    xVal = np.linspace(min(x), max(x), 100)
    # Compute corresponding y values using the polynomial equation
    yVal = slope * xVal + intercept

    # Construct a list of points representing the best-fit line
    bestFitLine = [(xVals, yVals) for xVals, yVals in zip(xVal, yVal)]

    return bestFitLine

def polynomialInterpolation(points, degree):
    xValues = [point[0] for point in points]
    yValues = [point[1] for point in points]

    # Create Vandermonde matrix
    A = np.vander(np.array(xValues), degree + 1)

    # Solve system of linear equations to find coefficients
    coefficients = np.linalg.solve(A, yValues)

    return coefficients


