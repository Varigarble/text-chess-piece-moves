import string
import chess_functions
# https://stackoverflow.com/questions/16060899/alphabet-range-on-python
''' Chessboard is absolute positions of 1-64'''

def piece_name_input():
    #  Get valid chess piece from user
    valid_pieces = ['B', 'Bishop', 'H', 'Horse', 'KI', 'King', 'KN', 'Knight', 'N', 'Knight', 'P', 'Pawn',
                    'Q', 'Queen', 'R', 'Rook']
    piece_entered = False
    while piece_entered == False:
        try:
            piece = input("State your piece: ")
            if not piece.isalpha():
                raise TypeError("requires letters only")
            if piece.upper() == 'K':
                raise Exception("ambiguous input")  # create a class CustomError(Exception) called KinghtError?
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
        print("Your piece is a kNight, NOT a horse")
        piece = 'N'
    elif p[:2] == 'KI':
        print("Your piece is a king")
        piece = 'K'
    elif p[:2] == 'KN':
        print("Your piece is a knight")
        piece = 'N'
    elif p[0] in valid_pieces:
        print(f"Your piece is a {valid_pieces[valid_pieces.index(p[0])+1]}.")
        piece = piece.upper()[0]

    return piece


piece = piece_name_input()
print("Here's the initial: ", piece)  # Confirming that the user input has been converted to a capital initial

def piece_color_input():
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
    # gets chess notation input and converts to absolute cell values
    row = int(input("State your row (1-8): "))
    raw_column = input("State your column (A-H): ").upper()
    column = (list(string.ascii_uppercase).index(raw_column)) + 1
    position = (row - 1) * 8 + column
    return position


position = locator()

#  summon piece functions from "chess_functions" here:
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
    attacked = chess_functions.black_pawn(position)
if piece == 'P' and color == 'W':
    attacked = chess_functions.white_pawn(position)

# draw board using array contents
row = 8
print("", " -" * 8)

print(row, "|", sep="", end="")

for all_squares in range(8, 0, -1):
    # global row
    for square in range((8 * (row - 1) + 1), (8 * (row - 1) + 9)):
        if square == position:
            print(piece, "|", sep="", end="")
        elif square not in attacked: # add not in capture?
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
        print("\n")
