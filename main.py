# Base file was created by user Dirk94 for ChessAI, all labeled functions are original/edited, unlabled are unedited
import board, pieces, ai, convertimage as ci, uniqueValues as uv
from move import Move

# Returns a move object based on the users input. Does not check if the move is valid.
# # Modify to read from picture ------------------------
global oldPieces 
oldPieces = ci.convertImage()

# function created by Henry Cussatt
def convertBoard(old, new):
    x,y = old
    if y > 0 and y < 60:
        row = '1'
    elif y > 59 and y < 120:
        row = '2'
    elif y > 119 and y < 180:
        row = '3'
    elif y > 179 and y < 240:
        row = '4'
    elif y > 239 and y < 300:
        row = '5'
    elif y > 299 and y < 360:
        row = '6'
    elif y > 359 and y < 420:
        row = '7'
    elif y > 419 and y < 480:
        row = '8'
    else:
        row = '9'

    if x > 134 and x <= 191:
        column = "H"
    elif x > 191 and x <= 248:
        column = "G"
    elif x > 248 and x <= 304:
        column = "F"
    elif x > 304 and x <= 361:
        column = "E"
    elif x > 361 and x <= 419:
        column = "D"
    elif x > 419 and x <= 476:
        column = "C"
    elif x > 476 and x <= 537:
        column = "B"
    elif x > 537 and x <= 601:
        column = "A"
    else:
        column ="P"
    
    oldPos = column + row
    x,y = new
    if y > 0 and y < 60:
        row = '1'
    elif y > 59 and y < 120:
        row = '2'
    elif y > 119 and y < 180:
        row = '3'
    elif y > 179 and y < 240:
        row = '4'
    elif y > 239 and y < 300:
        row = '5'
    elif y > 299 and y < 360:
        row = '6'
    elif y > 359 and y < 420:
        row = '7'
    elif y > 419 and y < 480:
        row = '8'
    else:
        row = '9'

    if x > 134 and x <= 191:
        column = "H"
    elif x > 191 and x <= 248:
        column = "G"
    elif x > 248 and x <= 304:
        column = "F"
    elif x > 304 and x <= 361:
        column = "E"
    elif x > 361 and x <= 419:
        column = "D"
    elif x > 419 and x <= 476:
        column = "C"
    elif x > 476 and x <= 537:
        column = "B"
    elif x > 537 and x <= 601:
        column = "A"
    else:
        column = "P"

    newPos = column + row
    return [oldPos, newPos]

# Original function coded by Dirk94, all lines before the try statement are coded by Henry Cussatt
def get_user_move():
    turn = ''
    oldPieces = ci.convertImage()
    while turn != 'c':
        turn = input("confirm placement or mark take? (c or t):  ")
        if turn == 't':
            oldPieces = ci.convertImage()

    move_str = ""
    i = 0
    old = (0,0)

    newPieces = ci.convertImage()
    unique = uv.findUniqueValues(oldPieces, newPieces)
    old = unique[0]
    new = unique[1]
    
    for item in convertBoard(old, new):
        move_str += item

    print(move_str)    
    try:
        xfrom = letter_to_xpos(move_str[0:1])
        yfrom = 8 - int(move_str[1:2]) # The board is drawn "upside down", so flip the y coordinate.
        xto = letter_to_xpos(move_str[2:3])
        yto = 8 - int(move_str[3:4]) # The board is drawn "upside down", so flip the y coordinate.
        key = '1'
        return Move(xfrom, yfrom, xto, yto)
    except ValueError:
        print("retake image. Example: A2 A4")
        return get_user_move()

# Returns a valid move based on the users input.
def get_valid_user_move(board):
    while True:
        move = get_user_move()
        valid = False
        possible_moves = board.get_possible_moves(pieces.Piece.WHITE)
        # No possible moves
        if (not possible_moves):
            return 0

        for possible_move in possible_moves:
            if (move.equals(possible_move)):
                valid = True
                break

        if (valid):
            break
        else:
            print("Invalid move.")
    return move

# Converts a letter (A-H) to the x position on the chess board.
def letter_to_xpos(letter):
    letter = letter.upper()
    if letter == 'A':
        return 0
    if letter == 'B':
        return 1
    if letter == 'C':
        return 2
    if letter == 'D':
        return 3
    if letter == 'E':
        return 4
    if letter == 'F':
        return 5
    if letter == 'G':
        return 6
    if letter == 'H':
        return 7

    raise ValueError("Invalid letter.")

#
# Entry point.
# Most of entry point written by user Dirk94, modified to also include setup for any image detection processes ran later in the program
board = board.Board.new()
print(board.to_string())

while True:
    move = get_valid_user_move(board)
    if (move == 0):
        key = '1'
        if (board.is_check(pieces.Piece.WHITE)):
            print("Checkmate. Black Wins.")
            break
        else:
            print("Stalemate.")
            break
    key = ''
    board.perform_move(move)

    print("User move: " + move.to_string())
    print(board.to_string())

    ai_move = ai.AI.get_ai_move(board, [])
    if (ai_move == 0):
        if (board.is_check(pieces.Piece.BLACK)):
            print("Checkmate. White wins.")
            break
        else:
            print("Stalemate.")
            break

    board.perform_move(ai_move)
    print("AI move: " + ai_move.to_string())
    print(board.to_string())
    oldPieces = ci.convertImage()
