from boardscan import snapshot
import math, cv2


def realPlayerTurn(board1, board2): #invoked when virtual player's turn is finished
    buttonPressed = False #signal sent from arduino to pi here
    initialSnap = snapshot("chessboard.png")
    squares = initialSnap[0]
    averages = initialSnap[1]
    for sq in initialSnap:
        print(sq.roiColor("chessboard.png"))
    if buttonPressed:
        finalSnap = snapshot()
        difference = board1.colorshift(board2)
        boardUpdate(difference)
    pass

def boardUpdate(diff):
    #POST to server
    pass


def virtualPlayerTurn():
    # poll server for virtual player to input their turn
    virtualTurn = ""
    # arduinoMovementFunction(virtualTurn)

def main(real, virtual):
    gameOver = False
    #...

    #start first move for white
    if real.isWhite():
        while not gameOver:
            realPlayerTurn()
            virtualPlayerTurn()
    else:
        while not gameOver:
            virtualPlayerTurn()
            realPlayerTurn()




def determineChanges2(oldAvgs, newAvgs, squares):
    

    largest = 0
    secondlargest = 0

    for i in range(len(squares)):

        sum = 0
        for j in range(0,3):
            sum += (newAvgs[i][j] - oldAvgs[i][j])**2
        difference = math.sqrt(sum)
        if difference > largest:
            largest = difference
            index = i
        elif difference > secondlargest:
            secondlargest = difference
            secondndIndex = i

    
    square1 = squares[index]
    square2 = squares[secondndIndex]

    if square1.base == "Black":
        if white:
            pass
        elif red:
            pass

        else: #black
            pass
    else:
        if black:
            pass

        elif red:
            pass

        else: #white
            pass


    if square2.base == "Black":
        if white:
            pass
        elif red:
            pass

        else: #black
            pass
    else:
        if black:
            pass

        elif red:
            pass

        else: #white
            pass

      


def determineChanges(self,previous, current, oldSq, newSq):
       '''
       Determines the change in color values within squares from picture to picture
       to infer piece movement
       '''

       copy = current.copy()
       
       largestSquare = 0
       secondLargestSquare = 0
       largestDist = 0
       secondLargestDist = 0
       stateChange = []

       # check for differences in color between the photos
       for sq in self.squares:
           colorPrevious = sq.roiColor(previous)
           colorCurrent = sq.roiColor(current)

           # distance in bgr values
           sum = 0
           for i in range(0,3):
               sum += (colorCurrent[i] - colorPrevious[i])**2

           distance = math.sqrt(sum)

           if distance > 25:
               stateChange.append(sq)
               
           if distance > largestDist:
               # update squares with largest change in color
               secondLargestSquare = largestSquare
               secondLargestDist = largestDist
               largestDist = distance
               largestSquare = sq

           elif distance > secondLargestDist:
               # update second change in color
               secondLargestDist = distance
               secondLargestSquare = sq


       
       # regular move two squares change state
       squareOne = largestSquare
       squareTwo = secondLargestSquare

       if True:
           squareOne.draw(copy, (255,0,0), 2)
           squareTwo.draw(copy, (255,0,0), 2)
           cv2.imshow("previous",previous)
           cv2.imshow("identified",copy)
           cv2.waitKey(0)
           cv2.destroyAllWindows()

       # get colors for each square from each photo
       oneCurr = squareOne.roiColor(current)
       twoCurr = squareTwo.roiColor(current)

       # calculate distance from empty square color value
       sumCurr1 = 0
       sumCurr2 = 0
       for i in range(0,3):
           sumCurr1 += (oneCurr[i] - squareOne.emptyColor[i])**2
           sumCurr2 += (twoCurr[i] - squareTwo.emptyColor[i])**2

       distCurr1 = math.sqrt(sumCurr1)
       distCurr2 = math.sqrt(sumCurr2)

       if distCurr1 < distCurr2:
           # square 1 is closer to empty color value thus empty
           squareTwo.state = squareOne.state
           squareOne.state = '.'
           

           self.move = squareOne.position + squareTwo.position

       else:
           # square 2 is currently empty
           squareOne.state = squareTwo.state
           squareTwo.state = '.'
           

                   
           self.move = squareTwo.position + squareOne.position

       return self.move


realPlayerTurn("","")