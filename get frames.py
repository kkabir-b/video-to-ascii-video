import cv2
vid = cv2.VideoCapture('bad_apple.mp4')
success,image = vid.read()
counter= 0
while success:
  cv2.imwrite("frame%d.jpg" % counter, image)    # save frame as JPEG file
  success,image = vid.read()
  counter += 1
