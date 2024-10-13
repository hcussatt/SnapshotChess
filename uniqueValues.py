# Written by Henry Cussatt, used to determine the move made in the picture and return it in a state useable by the chess engine
def findUniqueValues(oldBoard, newBoard):
    pairs = []
    unique = []
    for x,y in oldBoard["pawns"]:
        for nx,ny in newBoard["pawns"]:
            if abs(nx - x) < 50 and abs(ny - y) < 50:
                pairs.append((nx,ny))
                pairs.append((x,y))
    
    for x,y in oldBoard["rooks"]:
        for nx,ny in newBoard["rooks"]:
            if abs(nx - x) < 50 and abs(ny - y) < 50:
                pairs.append((nx,ny))
                pairs.append((x,y))
    
    for x,y in oldBoard["knights"]:
        for nx,ny in newBoard["knights"]:
            if abs(nx - x) < 50 and abs(ny - y) < 50:
                pairs.append((nx,ny))
                pairs.append((x,y))
    
    for x,y in oldBoard["bishops"]:
        for nx,ny in newBoard["bishops"]:
            if abs(nx - x) < 50 and abs(ny - y) < 50:
                pairs.append((nx,ny))
                pairs.append((x,y))
    
    for x,y in oldBoard["queen"]:
        for nx,ny in newBoard["queen"]:
            if abs(nx - x) < 50 and abs(ny - y) < 50:
                pairs.append((nx,ny))
                pairs.append((x,y))

    for x,y in oldBoard["king"]:
        for nx,ny in newBoard["king"]:
            if abs(nx - x) < 50 and abs(ny - y) < 50:
                pairs.append((nx,ny))
                pairs.append((x,y))

    for piece in oldBoard["pawns"]:
        if not (piece in pairs):
            unique.append(piece)

    for piece in newBoard["pawns"]:
        if not (piece in pairs):
            unique.append(piece)
    
    for piece in oldBoard["rooks"]:
        if not (piece in pairs):
            unique.append(piece)

    for piece in newBoard["rooks"]:
        if not (piece in pairs):
            unique.append(piece)
    
    for piece in oldBoard["knights"]:
        if not (piece in pairs):
            unique.append(piece)

    for piece in newBoard["knights"]:
        if not (piece in pairs):
            unique.append(piece)

    for piece in oldBoard["bishops"]:
        if not (piece in pairs):
            unique.append(piece)

    for piece in newBoard["bishops"]:
        if not (piece in pairs):
            unique.append(piece)
    
    for piece in oldBoard["queen"]:
        if not (piece in pairs):
            unique.append(piece)

    for piece in newBoard["queen"]:
        if not (piece in pairs):
            unique.append(piece)
    
    for piece in oldBoard["king"]:
        if not (piece in pairs):
            unique.append(piece)

    for piece in newBoard["king"]:
        if not (piece in pairs):
            unique.append(piece)

    if len(unique) == 2:
        return unique
    
    else:
        print(unique)
        print(len(unique))
        return [(0,0), (0,0)]

