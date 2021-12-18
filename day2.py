from reusablemethods import readStringFile


def day2_part1():
    directions = readStringFile("day2.txt")
    x = 0
    z = 0
    for dir in directions:
        direction = dir.split()
        if direction.__getitem__(0) == 'forward':
            x = moveForward(x, int(direction.__getitem__(1)))
        elif direction[0] == 'down':
            z = moveDown(z, int(direction.__getitem__(1)))
        elif direction[0] == 'up':
            z = moveUp(z, int(direction.__getitem__(1)))
        else:
            raise Exception("Input is invalid. Double check what you're doing ya dunce.")
    return [x, z]

def moveForward(x, distance):
    return x + distance


def moveDown(z, distance):
    if z + distance < 0:
        raise Exception("Can't go below 0")
    return distance + z


def moveUp(z, distance):
    return z - distance


def day2_part2():
    directions = readStringFile("day2.txt")
    #x, z, aim
    coords = [0,0,0]
    for dir in directions:
        direction = dir.split()
        if direction.__getitem__(0) == 'forward':
            coords = moveForward_2(coords, int(direction.__getitem__(1)))
        elif direction[0] == 'down':
            coords = moveDown_2(coords, int(direction.__getitem__(1)))
        elif direction[0] == 'up':
            coords = moveUp_2(coords, int(direction.__getitem__(1)))
        else:
            raise Exception("Input is invalid. Double check what you're doing ya dunce.")
    return coords


def moveForward_2(coords, distance):
    coords[0] = coords[0] + distance
    coords[1] = coords[1] + (coords[2] * distance)
    return coords


def moveDown_2(coords, distance):
    coords[2] = coords[2] + distance
    return coords


def moveUp_2(coords, distance):
    coords[2] = coords[2] - distance
    return coords

