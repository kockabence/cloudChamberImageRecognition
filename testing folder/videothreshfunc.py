import cv2

# default variables
videofile = '/home/bence/kodkamrademo.mp4'
blur = 1
threshold = 100


def videothresholding(videofile, blur, threshold):

    # open video file
    cap = cv2.VideoCapture(videofile)

    # get every frame
    while True:

        # capture frames
        ret, frame = cap.read()
        # convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # erosion -> dilation
        median = cv2.medianBlur(gray, blur)
        # binary thresholding
        ret, thresh1 = cv2.threshold(median, threshold, 255, cv2.THRESH_BINARY)

        # show feed
        cv2.imshow('frame', thresh1)

        # exit feed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

videothresholding(videofile, blur, threshold)
