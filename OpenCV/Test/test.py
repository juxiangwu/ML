import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read by means of OpenCV
# img = cv2.imread('kitten.jpg')
# cv2.imshow('ima', img)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()

# Plot using matplotlib
# b, g, r = cv2.split(img)
# img2 = cv2.merge([r, g, b])
# plt.imshow(img2)
# plt.xticks([]), plt.yticks([])
# plt.show()

# Simple video capture and converter
# capture = cv2.VideoCapture(0)
# while True:
#     ret, frame = capture.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
#
#     cv2.imshow('frame', gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# capture.release()
# cv2.destroyAllWindows()

# Capture from camera, flip every frame in vertical direction and saves it
# capture = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))
#
# while capture.isOpened():
#     ret, frame = capture.read()
#     if ret == True:
#         frame = cv2.flip(frame, 0)
#         out.write(frame)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# capture.release()
# out.release()
# cv2.destroyAllWindows()

# Drawing functions
# img = np.zeros([512, 512, 3])
# img = cv2.line(img, (0, 0), (512, 512), (255, 255, 0), 5)
# img = cv2.rectangle(img, (300, 30), (400, 200), (255, 0, 0), 10)
# img = cv2.ellipse(img, (120, 120), (20, 40), 0, 0, 360, (200, 120, 120), -1)
#
# font = cv2.FONT_HERSHEY_COMPLEX
# img = cv2.putText(img, 'Siavash', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
#
# cv2.imshow('image', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Mouse as a Paint-Brush
# drawing = False
# mode = True
# ix, iy = -1, -1
#
#
# def draw(event, x, y, flags, params):
#     global ix, iy, drawing, mode
#
#     if event == cv2.EVENT_MBUTTONDOWN:
#         drawing = True
#         ix, iy = x, y
#
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing is True and mode is True:
#             cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#         elif drawing is True and mode is False:
#             cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode is True:
#             cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
#         else:
#             cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
#
#
# img = np.zeros([512, 512, 3], np.uint8)
# cv2.namedWindow('window!')
# cv2.setMouseCallback('window!', draw)
#
# while 1:
#     cv2.imshow('image', img)
#     k = cv2.waitKey(1) & 0xFF
#     if k == ord('m'):
#         mode = not mode
#     elif k == 27:
#         break
#
# cv2.destroyAllWindows()

# Core Operations

# Simple addition
# img1 = cv2.imread('google.jpg')
# img2 = cv2.imread('android.jpg')
# # OpenCV function
# # dst = cv2.add(img1, img2)
# dst = cv2.addWeighted(img1, 0.1, img2, 0.9, 0)
# # Numpy addition
# # dst = img1 + img2
# cv2.imshow('mergedImage', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# Merge two photos
# img1 = cv2.imread('android.jpg')
# img2 = cv2.imread('kitten.jpg')
# # I want to put logo on top-left corner, So I create a ROI
# rows, cols, channels = img2.shape
# roi = img1[0:rows, 0:cols]
# # Now create a mask of logo and create its inverse mask also
# img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
# mask_inv = cv2.bitwise_not(mask)
# # Now black-out the area of logo in ROI
# img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# # Take only region of logo from logo image.
# img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
# # Put logo in ROI and modify the main image
# dst = cv2.add(img1_bg, img2_fg)
# img1[0:rows, 0:cols] = dst
# cv2.imshow('res', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Object Tracking
# cap = cv2.VideoCapture(0)
# while 1:
#     # Take each frame
#     _, frame = cap.read()
#     # Convert BGR to HSV
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     # define range of blue color in HSV
#     lower_blue = np.array([110, 50, 50])
#     upper_blue = np.array([130, 255, 255])
#     lower_green = np.array([50, 100, 100])
#     upper_green = np.array([70, 255, 255])
#     # Threshold the HSV image to get only blue colors
#     blueMask = cv2.inRange(hsv, lower_blue, upper_blue)
#     greenMask = cv2.inRange(hsv, lower_green, upper_green)
#     mask = cv2.bitwise_or(blueMask, greenMask)
#     # Bitwise-AND mask and original image
#     res = cv2.bitwise_and(frame, frame, mask=mask)
#     cv2.imshow('frame', frame)
#     cv2.imshow('mask', mask)
#     cv2.imshow('res', res)
#     k = cv2.waitKey(5) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()

# Uses gradient filters or High-pass filters, Sobel, Scharr, Laplacian
img = cv2.imread('sudoku.png')
laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.show()
