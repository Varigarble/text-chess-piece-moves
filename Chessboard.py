import string
# https://stackoverflow.com/questions/16060899/alphabet-range-on-python
''' Chessboard is absolute positions of 1-64'''
''' Piece input section 
TODO: try/except for ValueError for invalid input; 
'''

def piece_name_input():
    while True:
        try:
            piece = str(input("State your piece: "))
        except TypeError:
            raise TypeError("I know you're new to chess, but at least try to enter a word made of letters.")
        else:
            break
    p: str = piece.upper()

    if p[0] not in {"P", "R", "N", "KN", "H", "K", "KI", "B", "Q"}:
        raise ValueError("The chess pieces are: King, Queen, Bishop, Knight, Rook, and Pawn.")


    if p[0] == "P":
        print("Your piece is a pawn")

    if p[0] == "R":
        print("Your piece is a rook")

    if p[0] == "N" or p[:1] == "KN":
        print("Your piece is a knight")

    if p[0] == "H":
        print("Your piece is a knight, NOT a horse")

    if p[0] == "K" or p[:1] == "KI":
        print("Your piece is a king")

    if p[0] == "B":
        print("Your piece is a bishop")

    if p[0] == "Q":
        print("Your piece is a queen")
    return p


piece_name_input()


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
