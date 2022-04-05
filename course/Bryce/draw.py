import cv2 as cv
import numpy as np

blank = np.zeros((500, 500,3), dtype='uint8')
cv.imshow('Blank', blank)

img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# 1. paint the image a colour
blank[:] = 255, 255, 255
cv.imshow('Green', blank)

# 2. draw a rectangle

cv.rectangle(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (255, 0, 0), thickness=-1)
cv.imshow('Circle', blank)

# 4. draw a line
cv.line(blank, (0, 0), (blank.shape[0]//2, blank.shape[1]//2), (128, 255, 128), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (400, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)


cv.waitKey(0)
