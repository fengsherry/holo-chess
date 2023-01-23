import numpy as np
import cv2

class Square():
    def __init__(self, image, c1, c2, c3, c4, position, state='') -> None:
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.position = position
        
        #set base
        if (position[0] == 'a' or position[0] == 'c' or position[0] == 'e' or position[0] == 'g') and (int(position[1]) % 2 == 1):
            self.base = "Black"
        else:
            self.base = "White"
        
        
        # npArray of corners
        self.contour = np.array([c1,c2,c4,c3],dtype=np.int32)

        # Center of square
        M = cv2.moments(self.contour)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        # ROI for image differencing
        self.roi = (cx, cy)
        self.radius = 7

        self.emptyColor = self.roiColor(image)

        self.state = state


    def draw(self, image, color,thickness=2):

		# Formattign npArray of corners for drawContours
        ctr = np.array(self.contour).reshape((-1,1,2)).astype(np.int32)
        cv2.drawContours(image, [ctr], 0, color, 3)

    def drawROI(self, image, color, thickness = 1):

        cv2.circle(image, self.roi, self.radius, color,thickness)


    def roiColor(self, image):
        # Initialise mask
        maskImage = np.zeros((image.shape[0], image.shape[1]), np.uint8)
        # Draw the ROI circle on the mask
        cv2.circle(maskImage, self.roi, self.radius, (255, 255, 255), -1)
        # Find the average color
        average_raw = cv2.mean(image, mask=maskImage)[::-1]
        # Need int format so reassign variable
        average = (int(average_raw[1]), int(average_raw[2]), int(average_raw[3]))

        return average

    def classify(self, image):

        rgb = self.roiColor(image)

        sum = 0
        for i in range(0,3):
            sum += (self.emptyColor[i] - rgb[i])**2


        cv2.putText(image, self.position,self.roi,cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1,cv2.LINE_AA)