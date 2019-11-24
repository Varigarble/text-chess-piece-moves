""" This is a library of standard chess pieces and functions showing the possible moves of each."""

def white_pawn():
    global position

    attacked = {None}
    capture = {None}
    promotion = None  # placeholder for some other possibility
    invalid = None  # placeholder for some other possibility

    if (56 < position < 65):
        print("You must promote to a new queen, rook, bishop or knight")
        return promotion
    if (0 < position < 9):
        print("Pawns can't be there")
        return invalid
    if (8 < position < 57):
        attacked.add(position + 1)
        if ((position + 7) % 8) != 0:
            capture.add(position + 7)
        if ((position + 8) % 8) != 0:
            capture.add(position + 9)
    if (8 < position < 17):
        attacked.add(position + 2)

    return attacked, capture

# attacked, capture = white_pawn()
# print(attacked)
# print(capture)

def black_pawn():

    global position

    attacked = {None}
    capture = {None}
    promotion = None  # placeholder for some other possibility
    invalid = None  # placeholder for some other possibility

    if (0 < position < 9):
        print("You must promote to a new queen, rook, bishop or knight")
        return promotion
    if (56 < position < 65):
        print("Pawns can't be there")
        return invalid
    if (8 < position < 57):
        attacked.add(position - 1)
        if ((position - 8) % 8) != 0:
            capture.add(position - 7)
        if ((position - 9) % 8) != 0:
            capture.add(position - 9)
    if (48 < position < 57):
        attacked.add(position - 2)

    return attacked, capture

# attacked, capture = black_pawn()
# print(attacked)
# print(capture)

def rook():

    global position

    attacked = {None}
    # row
    while (position > 1) and (position - 1) % 8 != 0:
        attacked.add(position - 1)
        position -= 1
    position = reset_position

    while (position < 64) and (position % 8 != 0):
        attacked.add(position + 1)
        position += 1
    # reset_position = position <- set at beginning
    position = reset_position
    # column
    while ((position - 8) > 0) and (position > 8):
        attacked.add(position - 8)
        position -= 8
    position = reset_position
    while (position + 8) < 65:
        attacked.add(position + 8)
        position += 8
    position = reset_position
    return attacked

def bishop():
    # TODO: check for valid inputs; see if advantage to lists instead of sets; combine row, col?
    global position

    attacked = {None}

    # ll to ur diagonal
    while (position > 1) and (position < 65) and (((position - 1) % 8) != 0):
        if (position - 9) > 0:
            attacked.add(position - 9)
        position -= 9
    position = reset_position
    while (position > 0) and (position < 64) and ((position % 8) != 0):
        if (position + 9) < 65 and ((position + 9) > position % 8):
            attacked.add(position + 9)
        position += 9
    position = reset_position

    # ul to lr diagonal
    while (position > 1) and (position < 64) and ((position % 8) != 0):
        if (position - 7) > 0:
            attacked.add(position - 7)
        position -= 7
    position = reset_position
    while (position > 1) and (position < 64) and (((position + 7) % 8) != 0):
        if (position + 7) < 65:
            attacked.add(position + 7)
        position += 7
    position = reset_position
    return attacked

def queen():
    attacked = rook() | bishop()
    return attacked

def knight(position):
    position
    reset_position = position
    attacked = {None}

    # vertical up & left/right
    if (((position + 15) % 8) != 0) and (position + 15 < 64):
        attacked.add(position + 15)
    position = reset_position
    if (((position + 16) % 8) != 0) and (position + 17 < 64):
        attacked.add(position + 17)
    position = reset_position

    # horizontal left & up/down
    if (((position - 1) % 8) != 0) and (((position - 2) % 8) != 0) \
            and (2 < position < 57):
        attacked.add(position + 6)
    position = reset_position
    if (((position - 1) % 8) != 0) and (((position - 2) % 8) != 0) \
            and (10 < position < 65):
        attacked.add(position - 10)
    position = reset_position

    # horizontal right & up/down
    if ((position % 8) != 0) and (((position + 1) % 8) != 0) \
            and (position < 55):
        attacked.add(position + 10)
    position = reset_position
    if ((position % 8) != 0) and (((position + 1)) % 8 != 0) \
            and (8 < position < 63):
        attacked.add(position - 6)
    position = reset_position

    # vertical down & left/right
    if (((position - 17) % 8) != 0) and (position - 17 > 0):
        attacked.add(position - 17)
    position = reset_position
    if (((position - 16) % 8) != 0) and (position - 15 > 1):
        attacked.add(position - 15)
    position = reset_position

    return attacked

def white_king():
    global position
    attacked = {None}

    if position == 61:
        attacked.add(63)
    # upper row
    for x in range(position + 7, position + 9):
        if (position < 57) and (((position + 7) % 8) != 0) and (((position + 7) % 8) != 0):
            attacked.add(x)

    return attacked


