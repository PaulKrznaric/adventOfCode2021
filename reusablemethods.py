def readStringFile(file_name):
    file = open(file_name, 'r')
    list = [line.rstrip('\n') for line in file]
    file.close()
    return list

