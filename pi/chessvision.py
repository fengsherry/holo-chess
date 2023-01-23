import cv2
import matplotlib.pyplot as plt
import numpy as np
import keyboard

board = np.array([["R","N","B","Q","K","B","N","R"],
                  ["P","P","P","P","P","P","P","P"],
                  ["E","E","E","E","E","E","E","E"],
                  ["E","E","E","E","E","E","E","E"],
                  ["E","E","E","E","E","E","E","E"],
                  ["E","E","E","E","E","E","E","E"],
                  ["P","P","P","P","P","P","P","P"],
                  ["R","N","B","Q","K","B","N","R"]])

im = cv2.imread('opencv/boardinitial.png')
vidcap = cv2.VideoCapture(1)

class makesquare:
    def __init__(self, image, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        mx = int((x1+x2)/2)
        my = int((y1+y2)/2)
        
        self.center = (mx, my)
        self.radius = 9

        self.colour = self.avgColour(image)

        
    def avgColour(self, image):
        # Initialise mask
        maskImage = np.zeros((image.shape[0], image.shape[1]), np.uint8)
        # Draw the ROI circle on the mask
        cv2.circle(maskImage, self.center, self.radius, (255, 255, 255), -1)
        # Find the average color
        average_raw = cv2.mean(image, mask=maskImage)[::-1]
        # Need int format so reassign variable
        average = (int(average_raw[1]), int(average_raw[2]), int(average_raw[3]))
        return average

square1 = makesquare(im, 50, 50, 100, 100)
print(square1.center)
print(square1.colour)
cv2.imshow("image", im)


        
#check if connection with camera is successfully
if vidcap.isOpened():
    ret, frame = vidcap.read()  #capture a frame from live video
    #check whether frame is successfully captured
    
    if ret:
        
        # continue to display window until 'q' is pressed
        while(True):
            ret, frame = vidcap.read() #capture a frame from live video
            cv2.imshow("Frame",frame)
            
            button = cv2.waitKey(0)
            if button == ord('q'):
                break
            elif button == ord('a'):
                img = frame
                cv2.imwrite("Frame.jpg", frame)
                cv2.imshow("Frame",frame)
            
    #print error if frame capturing was unsuccessful
    else:
        print("Error : Failed to capture frame")

# print error if the connection with camera is unsuccessful
else:
    print("Cannot open camera")



