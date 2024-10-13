# Coded by Henry Cussatt, uses concepts and certain lines of code from image processing tutorial by Tonichi Edeza, and GeeksForGeeks  OpenCV tutorials
# https://towardsdatascience.com/image-processing-with-python-color-isolation-for-beginners-3b472293335b
# https://www.geeksforgeeks.org/how-to-detect-shapes-in-images-in-python-using-opencv/
import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from skimage.io import imshow, imread, imsave
from skimage.color import rgb2hsv, hsv2rgb

def convertImage(): 
    # reading image 
    board = imread('showPhoto/static/test.png')
    filter = ((board[:,:,0] < 100) & (board[:,:,1] < 95) & (board[:,:,2] > 90))

    convertedBoard = board.copy()

    convertedBoard[:, :, 0] = convertedBoard[:,:,0] * filter
    convertedBoard[:, :, 1] = convertedBoard[:,:,1] * filter
    convertedBoard[:, :, 2] = convertedBoard[:,:,2] * filter

    
    plt.imsave("showPhoto/static/converted.png", cv2.bitwise_not(convertedBoard))
    convertedBoard = imread("showPhoto/static/converted.png")
    convertedBoard2 = convertedBoard.copy()
    filter2 = ((convertedBoard[:,:,0] > 150) & (convertedBoard[:,:,1] > 150) & (convertedBoard[:,:,2] < 150))

    convertedBoard2[:, :, 0] = convertedBoard2[:,:,0] * filter2
    convertedBoard2[:, :, 1] = convertedBoard2[:,:,1] * filter2
    convertedBoard2[:, :, 2] = convertedBoard2[:,:,2] * filter2

    gray_board = cv2.cvtColor(cv2.bitwise_not(convertedBoard2), cv2.COLOR_BGR2GRAY)
    # converting image into grayscale image 
    gray = gray_board
    # setting threshold of gray image 
    _, threshold = cv2.threshold(gray, 227, 255, cv2.THRESH_BINARY) 
    
    # using a findContours() function 
    contours, _ = cv2.findContours( 
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    i = 0
    
    pieces = { "pawns" : [], "rooks" : [], "knights" : [], "bishops" : [], "queen" : [], "king" : []}
    # list for storing names of shapes 
    for contour in contours: 
    
        # here we are ignoring first counter because  
        # findcontour function detects whole image as shape 
        if i == 0: 
            i = 1
            continue
        if cv2.arcLength(contour, True) < 30 or cv2.arcLength(contour, True) > 130:
            continue
        if cv2.contourArea(contour) < 350:
            continue
        # cv2.approxPloyDP() function to approximate the shape 
        approx = cv2.approxPolyDP( 
            contour, 0.038 * cv2.arcLength(contour, True), True) 
        
        # using drawContours() function 
        cv2.drawContours(board, [contour], 0, (0, 0, 255), 5) 
    
        # finding center point of shape 
        M = cv2.moments(contour) 
        if M['m00'] != 0.0: 
            x = int(M['m10']/M['m00']) 
            y = int(M['m01']/M['m00']) 
        else:
            x = 0
            y = 0
        
    
        if x < 130 or x > 601 or y < 30:
            continue
        # putting shape name at center of each shape 
        if len(approx) == 3:
            cv2.putText(board, 'Pawn', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
            print(f"Found pawn at coordinates ({x}, {y})")
            pieces["pawns"].append((x,y))

        if len(approx) == 4:
            cv2.putText(board, 'Rook', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
            print(f"Found Rook at coordinates ({x}, {y})")
            pieces["rooks"].append((x,y))


        if len(approx) == 5:
            cv2.putText(board, 'Knight', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
            print(f"Found Knight at coordinates ({x}, {y})")
            pieces["knights"].append((x,y))

        if len(approx) == 6:
            cv2.putText(board, 'Bishop', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
            print(f"Found Bishop at coordinates ({x}, {y})")
            pieces["bishops"].append((x,y))
        
        if len(approx) == 7:
            cv2.putText(board, 'Queen', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
            print(f"Found queen at coordinates ({x}, {y})")
            pieces["queen"].append((x,y))

        if len(approx) == 8:
            cv2.putText(board, 'King', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
            print(f"Found king at coordinates ({x}, {y})")
            pieces["king"].append((x,y))
        
    
    # displaying the image after drawing contours 
    cv2.imwrite('showPhoto/static/test.jpg', board)


    # copy shapes to last picture

    print(pieces)
    return pieces

if __name__ == "__main__":
    convertImage()


