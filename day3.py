from reusablemethods import readStringFile, convert_from_binary


def day3():
    binaryInput = readStringFile("day3.txt")

    mostCommon = []
    for i in range(0, len(binaryInput[0])):
        mostCommon.append(0)

    # [epsilon, gamma]
    finalBinaryValues = ["", ""]

    for binary in binaryInput:
        for i in range(0, len(binary)):
            if int(binary[i]) == 1:
                mostCommon[i] = mostCommon[i] + 1
            else:
                mostCommon[i] = mostCommon[i] - 1

    for digit in mostCommon:
        if (digit > 0):
            finalBinaryValues[0] = __append_bin_value(finalBinaryValues[0], "1")
            finalBinaryValues[1] = __append_bin_value(finalBinaryValues[1], "0")
        else:
            finalBinaryValues[0] = __append_bin_value(finalBinaryValues[0], "0")
            finalBinaryValues[1] = __append_bin_value(finalBinaryValues[1], "1")

    return convert_from_binary(finalBinaryValues[0]) * convert_from_binary(finalBinaryValues[1])


def __append_bin_value(original, append):
    return original + append


