# import the opencv library
import cv2


def init_image(img1, scale, blur):  # Initialising image width and blur
    img_scaled = cv2.resize(img1, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    blurred = cv2.GaussianBlur(img_scaled, (blur, blur), cv2.BORDER_DEFAULT)
    return blurred


# define a video capture object
vid = cv2.VideoCapture(0)

while True:

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame3 = cv2.equalizeHist(frame2)
    # frame4 = cv2.Laplacian(frame3, cv2.CV_64F)
    frame4 = cv2.Sobel(frame3, cv2.CV_64F, 0, 1, ksize=9)
    frame5 = 255-frame4
    # frame5 = init_image(frame4, 1, 3)
    # frame5 = cv2.equalizeHist(frame4)
    # Display the resulting frame
    cv2.imshow('frame', frame5)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
