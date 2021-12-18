def readStringFile(file_name):
    file = open(file_name, 'r')
    list = [line.rstrip('\n') for line in file]
    file.close()
    return list


def convert_from_binary(binaryNumber):
    length = len(binaryNumber)
    value = 0
    for character in binaryNumber:
        intChar = int(character)
        value = value + intChar * pow(2, length - 1)
        length = length - 1
    return value
