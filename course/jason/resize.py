import cv2 as cv

# img = cv.imread('../resources/photos/cat.jpg')
# cv.imshow('Cat', img)

def rescale_frame(frame, scale=0.75):
    # width of image
    width = int(frame.shape[1] * scale)

    # height of image
    height = int(frame.shape[0] * scale)

    # creates a tuple of width and height
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('../resources/videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame)

    # First video is fullsized, second is resized
    # cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


# def show():
#     capture = cv.VideoCapture('../resources/videos/dog.mp4')

#     while True:
#         frame = capture.read()

#         frame_resized = rescale_frame(frame)

#         cv.imshow('Video', frame)
#         cv.imshow('Video Resized', frame_resized)

#         if cv.waitKey(20) & 0xFF == ord('d'):
#             break

#     capture.release()
#     cv.destroyAllWindows()


# show()

