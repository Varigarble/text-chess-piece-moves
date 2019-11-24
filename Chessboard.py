import string
# https://stackoverflow.com/questions/16060899/alphabet-range-on-python
''' Chessboard is absolute positions of 1-64'''

def piece_name_input():
    #  Get valid chess piece from user
    # TODO: convert piece entry to standard initial in valid_pieces
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

    return piece


piece = piece_name_input()

print(piece) #  Will need to be a standard initial in valid_pieces

def piece_color_input():
    color: str = input("State your color: ").upper()

    if color[0] == "B":
        print("Your piece is black")

    if color[0] == "W":
        print("Your piece is white")

piece_color_input()


def locator():
    # gets chess notation input and converts to absolute cell values
    row = int(input("State your row (1-8): "))
    raw_column = input("State your column (A-H): ").upper()
    column = (list(string.ascii_uppercase).index(raw_column)) + 1
    position = (row - 1) * 8 + column
    return position


locator()

position = locator()
reset_position = position
# sample board inputs from piece function outputs:
attacked = {1, 34, 35, 36, 37, 38, 39, 40, 9, 41, 17, 49, 25, 57}
capture = {9, 11}
raw_piece = "rook"
piece = raw_piece[0].upper()
position = 33

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
