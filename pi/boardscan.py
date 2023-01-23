import numpy as np
import cv2, imutils
import sys, math
from line import Line
from square import Square

def intersection(v, h):
    # x1,y1,x2,y2 --> [[0]],[[1]], [[2]], [[3]]

    #Cramer formula to find point of intersection
    x = ((v[[0]]*v[[3]] - v[[1]]*v[[2]])*(h[[0]]-h[[2]]) - (v[[0]]-v[[2]])*(h[[0]]*h[[3]] - h[[1]]*h[[2]]))/ ((v[[0]]-v[[2]])*(h[[1]]-h[[3]]) - (v[[1]]-v[[3]])*(h[[0]]-h[[2]]))
    y = ((v[[0]]*v[[3]] - v[[1]]*v[[2]])*(h[[1]]-h[[3]]) - (v[[1]]-v[[3]])*(h[[0]]*h[[3]] - h[[1]]*h[[2]]))/ ((v[[0]]-v[[2]])*(h[[1]]-h[[3]]) - (v[[1]]-v[[3]])*(h[[0]]-h[[2]]))
    x = int(x)
    y = int(y)
    return x, y


def makeSquares(corners, cdst):
    print(len(corners))
    #sort corners by row
    corners.sort(key=lambda x: x[0])
    rows = [[],[],[],[],[],[],[],[],[]]
    r = 0
    for c in range(0, 81):
        if c > 0 and c % 9 == 0:
            r = r + 1
            print(rows[r])
            print(corners[c])
        rows[r].append(corners[c])

    #sort corners by column
    for r in rows:
        r.sort(key=lambda y: y[1])
    
    # initialize squares
    letters = ['a','b','c','d','e','f','g','h']
    numbers = ['1','2','3','4','5','6','7','8']
    squares = []
    avgs = []
    for r in range(0,8):
        for c in range (0,8):
            c1 = rows[r][c]
            c2 = rows[r][c + 1]
            c3 = rows[r + 1][c]
            c4 = rows[r + 1][c + 1]

            position = letters[r] + numbers[7-c]
            newSquare = Square(cdst,c1,c2,c3,c4,position)
            newSquare.draw(cdst,(0,0,255),2)
            newSquare.drawROI(cdst,(0,255,0),2)
            newSquare.classify(cdst)
            avg = newSquare.roiColor(cdst)
            avgs.append(avg)
            squares.append(newSquare)
    
    cv2.imshow('squares', cdst)
    cv2.waitKey(0)

    return squares, avgs


def snapshot(picture):
    img = cv2.imread(cv2.samples.findFile(picture)) #picture
    if img is None:
        sys.exit("Could not read the image.")
    cv2.imshow("Display window", img)



    # resize image and convert to grayscale
    resized = imutils.resize(img, width=500, height = 500)


    gray = cv2.cvtColor(resized, cv2.COLOR_RGB2GRAY)

    # adaptive thresholding to keep all pixels within thresholds black/white
    adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 125, 1)
    cv2.imshow("Thresholding", adaptive)




    # canny edge detection
    canny = cv2.Canny(adaptive, 100, 200, None, 3)
    cv2.imshow("canny", canny)



    # Copy edges to the images that will display the results in BGR
    cdst = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)


    lines = cv2.HoughLinesP(canny, 1, np.pi / 180, 100, np.array([]), 100, 80)
    x, y, z = lines.shape # x = number of lines, z = x or y axis
    for i in range(x):
                cv2.line(cdst, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0,255,0),2,cv2.LINE_AA)

    cv2.imshow("Hough Lines", cdst)
    cv2.waitKey(0)



    print(lines.shape)
    # sort horizontal and vertical lines
    horizontal = []
    vertical = []

    for line in range(x):
        [[x1,y1,x2,y2]] = lines[line]
        newLine = Line(x1, x2, y1, y2)
        # determine orientation
        if abs(x2-x1) > abs(y2-y1):
            horizontal.append(newLine)
        else:
            vertical.append(newLine)



    # find corners at each intersection
    corners = []
    for v in vertical:
        for h in horizontal:
            p1, p2 = v.intersection(h)
            corners.append([p1, p2])
    
                
    for d in corners:
        cv2.circle(cdst, (d[0],d[1]), 10, (255,0,0))


    cv2.imshow("Corners",cdst)

    return makeSquares(corners, cdst)




if __name__ == '__main__':
    snapshot()

