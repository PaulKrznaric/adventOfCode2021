from reusablemethods import readStringFile


def day2():
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
