def turtle(coord, direction):
    buf = yield direction
    x, y = coord
    while buf:
        match buf:
            case  'f':
                match direction:
                    case 0:
                        x += 1
                    case 1:
                        y += 1
                    case 2:
                        x -= 1
                    case 3:
                        y -= 1
            case 'l':
                direction = (direction + 1) % 4
            case 'r':
                direction = (direction - 1) % 4
        buf = yield (x, y)
