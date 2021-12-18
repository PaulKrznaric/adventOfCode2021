from reusablemethods import readStringFile


def day2_part1():
    directions = readStringFile("day2.txt")
    x = 0
    z = 0
    for dir in directions:
        direction = dir.split()
        if direction.__getitem__(0) == 'forward':
            x = __move_forward(x, int(direction.__getitem__(1)))
        elif direction[0] == 'down':
            z = __move_down(z, int(direction.__getitem__(1)))
        elif direction[0] == 'up':
            z = __move_up(z, int(direction.__getitem__(1)))
        else:
            raise Exception("Input is invalid. Double check what you're doing ya dunce.")
    return [x, z]


def __move_forward(x, distance):
    return x + distance


def __move_down(z, distance):
    if z + distance < 0:
        raise Exception("Can't go below 0")
    return distance + z


def __move_up(z, distance):
    return z - distance


def day2_part2():
    directions = readStringFile("day2.txt")
    # x, z, aim
    coords = [0, 0, 0]
    for direction in directions:
        direction = direction.split()
        if direction.__getitem__(0) == 'forward':
            coords = __move_forward_v2(coords, int(direction.__getitem__(1)))
        elif direction[0] == 'down':
            coords = __move_down_v2(coords, int(direction.__getitem__(1)))
        elif direction[0] == 'up':
            coords = __move_up_v2(coords, int(direction.__getitem__(1)))
        else:
            raise Exception("Input is invalid. Double check what you're doing ya dunce.")
    return coords


def __move_forward_v2(coords, distance):
    coords[0] = coords[0] + distance
    coords[1] = coords[1] + (coords[2] * distance)
    return coords


def __move_down_v2(coords, distance):
    coords[2] = coords[2] + distance
    return coords


def __move_up_v2(coords, distance):
    coords[2] = coords[2] - distance
    return coords
