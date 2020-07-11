import string
import chess_functions
"""Chessboard is a grid of 1-64. Uncomment code below to print a grid as numpy array."""
# import numpy as np
# print(np.flip((np.arange(1, 65).reshape(8, 8)), 0))

def piece_name_input():
    # Get valid chess piece from user
    valid_pieces = ['B', 'Bishop', 'C', 'Castle', 'H', 'Horse', 'KI', 'King', 'KN', 'Knight', 'N', 'Knight', 'P', 'Pawn',
                    'Q', 'Queen', 'R', 'Rook']
    piece_entered = False
    while piece_entered == False:
        try:
            piece = input("State your piece: ")
            if not piece.isalpha():
                raise TypeError("requires letters only")
            if piece.upper() == 'K':
                raise Exception("ambiguous input")  # class KinghtError(ValueError):
            if (piece.upper()[0] not in valid_pieces) and (piece.upper()[:2] not in valid_pieces):
                raise ValueError("not a real piece")
        except TypeError:
            print("Piece names only use letters.")
            piece_entered = False
        except ValueError:
            print("The chess pieces are: King, Queen, Bishop, Knight, Rook, and Pawn.")
            piece_entered = False
        except Exception:
            print("\"K\" what? Be more specific.")
        else:
            if piece.isalpha() and ((piece.upper()[0] in valid_pieces) or (piece.upper()[:2]) in valid_pieces):
                piece_entered = True

    #  Display valid entry
    p: str = piece.upper()

    if p[0] == "H":
        print("Your piece is a Knight, NOT a horse")
        piece = 'N'
    if p[0] == "C":
        print("Your piece is a Rook, a.k.a. a Castle")
        piece = 'R'  # Thanks, April!
    elif p[:2] == 'KI':
        print("Your piece is a King")
        piece = 'K'
    elif p[:2] == 'KN':
        print("Your piece is a Knight")
        piece = 'N'
    elif p[0] in valid_pieces:
        print(f"Your piece is a {valid_pieces[valid_pieces.index(p[0])+1]}.")
        piece = piece.upper()[0]

    return piece


piece = piece_name_input()
print("Here's the chess notation: ", piece)

def piece_color_input():
    # Get valid color from user
    valid_in = False
    while valid_in == False:
        try:
            color: str = input("State your color: ").upper()
            if not color.isalpha():
                raise TypeError("requires letters only")
            if (color[0] != 'B') and (color[0] != 'W'):
                raise ValueError("invalid color")
        except TypeError:
            print("Enter color names with only letters.")
            valid_in = False
        except ValueError:
            print("Enter \"Black\" or \"White.\"")
            valid_in = False
        except Exception:
            print("I'm not sure what's wrong.")
        else:
            if color.isalpha() and ((color[0] == 'B') or (color[0] == 'W')):
                valid_in = True

    if color[0] == "B":
        print("Your piece is black")
        color = 'B'
    if color[0] == "W":
        print("Your piece is white")
        color = 'W'
    return color

color = piece_color_input()


def locator():
    # gets chess notation coordinate input and converts to cell values
    valid_row = False
    valid_col = False
    while valid_row == False:
        try:
            row = int(input("State your row (1-8): "))
            if type(row) != int:
                raise TypeError("wrong input")
            if not 0 < row < 9:
                raise ValueError("off the grid")
        except TypeError:
            print("Enter the input indicated")
            valid_row = False
        except ValueError:
            print("You have to be on the board to play")
        else:
            valid_row = True

    while valid_col == False:
        try:
            raw_column = input("State your column (A-H): ").upper()
            if not raw_column.isalpha():
                raise TypeError("wrong input")
            if raw_column not in string.ascii_uppercase[0:8]:
                raise ValueError("off the grid")
        except TypeError:
            print("Enter the input indicated")
            valid_col = False
        except ValueError:
            print("You have to be on the board to play")
            valid_col = False
        else:
            valid_col = True

    column = (list(string.ascii_uppercase).index(raw_column)) + 1
    position = (row - 1) * 8 + column
    return position


position = locator()

#  summon piece functions from "chess_functions" here:
if piece != 'P':
    capture = {None}
if piece == 'N':
    attacked = chess_functions.knight(position)
if piece == 'B':
    attacked = chess_functions.bishop(position)
if piece == 'R':
    attacked = chess_functions.rook(position)
if piece == 'Q':
    attacked = chess_functions.queen(position)
if piece == 'K':
    attacked = chess_functions.king(position, color)
if piece == 'P' and color == 'B':
    if 8 < position < 57:
        attacked = chess_functions.black_pawn(position)[0]
        capture = chess_functions.black_pawn(position)[1]
    elif position > 56:
        print("Black pawns can't be on that row")
        position = None
        attacked = {None}
        capture = {None}
    else:
        attacked = chess_functions.black_pawn(position)
        capture = {None}
if piece == 'P' and color == 'W':
    if 57 > position > 8:
        attacked = chess_functions.white_pawn(position)[0]
        capture = chess_functions.white_pawn(position)[1]
    elif position < 9:
        print("White pawns can't be on that row")
        position = None
        attacked = {None}
        capture = {None}
    else:
        attacked = chess_functions.white_pawn(position)
        capture = {None}

# draw board
row = 8
print("", " -" * 8)

print(row, "|", sep="", end="")

for all_squares in range(8, 0, -1):
    for square in range((8 * (row - 1) + 1), (8 * (row - 1) + 9)):
        if square == position:
            print(piece, "|", sep="", end="")
        elif (square not in attacked) and (square not in capture):
            print(" ", "|", sep="", end="")
        elif square in attacked:
            print("X", "|", sep="", end="")
        elif square in capture:
            print("C", "|", sep="", end="")
    row -= 1
    print("\n", " -" * 8)
    if row > 0:
        print(row, "|", sep="", end="")
    if row == 0:
        print(" ", end="")
        for ltr in string.ascii_uppercase[0:8]:
            print("", ltr, end="")
        #  print("\n")
