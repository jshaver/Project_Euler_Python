from Crypto.Util.number import bignum
from Tools import *


# region Problems 1-10
def solve_001(upperLimit: int):
    result = 0
    for i in range(1, upperLimit):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


def solve_002(upperLimit: int):
    result = 0
    for i in range(1, upperLimit + 1):
        num = getNthFibonacciTerm(i)
        # print(str(i) + "  :  " + str(num))
        if num > upperLimit:
            break
        if num % 2 == 0:
            result += num
    return result


def solve_003(inputNumber: int):
    result = 0
    primeComponents = getPrimeComponents(inputNumber)
    if len(primeComponents) > 0:
        for i in range(0, len(primeComponents)):
            if primeComponents[i] > result:
                result = primeComponents[i]
    return result


def solve_004(inputStart: int, inputRange: int):
    result = 0
    for i in range(inputStart, inputStart - inputRange, -1):
        for j in range(inputStart, inputStart - inputRange, -1):
            product = i * j
            if isPalindrome(product) and product > result:
                result = product
                # print("Palindrome found: " + str(i) + " and " + str(j) + " = " + str(product))
    return result


def solve_006(inputLimit: int):
    result = 0
    sumOfSquares = 0
    sumTotal = 0
    for i in range(1, inputLimit + 1):
        sumOfSquares += pow(i, 2)
        sumTotal += i
    squareOfSum = pow(sumTotal, 2)
    result = squareOfSum - sumOfSquares
    return result


def solve_007(arg: int):
    result = getNthPrimeNumber(arg)
    return result


def solve_008(inputLen: int):
    result = 0
    activeList = []
    with open("Input/p008_numberString.txt") as inputStream:
        while len(activeList) < inputLen:
            activeList.append(int(inputStream.read(1)))
        for i in range(0, 1000-inputLen):
            activeProduct = 1
            for j in range(0, inputLen):
                activeProduct *= activeList[j]
            if activeProduct > result:
                result = activeProduct
                # print("Iteration " + str(i) + " : " + str(result) + "  :  " + str(activeList))
            activeList.pop(0)
            activeList.append(int(inputStream.read(1)))
    return result


def solve_009(inputLimit: int):
    result = 0
    for a in range(1, inputLimit):
        for b in range(a, inputLimit):
            c = inputLimit - (a + b)
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                # print("Result found: " + str(a) + " + " + str(b) + " = " + str(c))
                result = a * b * c
                return result
            elif pow(a, 2) + pow(b, 2) > pow(c, 2):
                break
    return result


def solve_010(inputLimit: int):
    result = 0
    for i in range(1, inputLimit):
        prime = getNthPrimeNumber(i)
        if prime < inputLimit:
            result += prime
        else:
            break
    return result
# endregion


# region Problems 11-20
def solve_011():
    result = 0
    with open("Input/p011_matrix.txt") as inputStream:
        matrix = []
        line = inputStream.readline()
        while line != '':
            array = []
            tokens = line.split()
            for i in range(0, len(tokens)):
                array.append(int(tokens[i]))
            matrix.append(array)
            line = inputStream.readline()

    # analyze horizontally
    for y in range(0, 20):
        for x in range(0, 17):
            product = matrix[y][x] * matrix[y][x + 1] * matrix[y][x + 2] * matrix[y][x + 3]
            if product > result:
                result = product

    # analyze vertically
    for y in range(0, 17):
        for x in range(0, 20):
            product = matrix[y][x] * matrix[y + 1][x] * matrix[y + 2][x] * matrix[y + 3][x]
            if product > result:
                result = product

    # analyze diagonally-right
    for y in range(0, 17):
        for x in range(0, 17):
            product = matrix[y][x] * matrix[y + 1][x + 1] * matrix[y + 2][x + 2] * matrix[y + 3][x + 3]
            if product > result:
                result = product

    # analyze diagonally-left
    for y in range(3, 20):
        for x in range(0, 17):
            product = matrix[y][x] * matrix[y - 1][x + 1] * matrix[y - 2][x + 2] * matrix[y - 3][x + 3]
            if product > result:
                result = product

    return result


def solve_012():
    result = 0
    largestCount = 0
    for i in range(1, 50001):
        tri = getNthTriangleTerm(i)
        triFactors = getFactors(tri)
        if len(triFactors) > largestCount:
            # print(str(i) + " : " + str(tri) + " : # of factors: " + str(len(triFactors)))
            largestCount = len(triFactors)
        if largestCount > 500:
            result = tri
            break
    return result


def solve_013():
    result = 0
    numberArray = []
    with open("Input/p013_numbers.txt") as inputStream:
        line = inputStream.readline()
        while line != '':
            numberArray.append(bignum(line))
            line = inputStream.readline()

    for i in range(0, len(numberArray)):
        result += numberArray[i]

    return result


def solve_014():
    result = [1, 0]
    for x in range(2, 1000000):
        count = getCollatzStepCount(x)
        if count > result[1]:
            result = [x, count]
        # print(str(x) + " : " + str(count))
        # if (x%100000) == 0:
        #     print(str(result[0]) + " : " + str(result[1]))
    return result


def solve_015():
    result = getPathCount(20, 20)
    return result


def solve_016():
    result = 0
    bigNumber = 2 ** 1000
    # print(str(bigNumber))
    bigString = str(bigNumber)
    for c in bigString:
        result += int(c)

    # while bigNumber > 0:
    #   result += int(bigNumber) % 10
    #   bigNumber = Decimal(bigNumber/Decimal(10))  # can't do this, changes type to float and loss of precision
    return result


def solve_017():
    result = 0
    for i in range(1, 1001):
        words = toWords(i)
        # print(words)
        words = words.replace("-", "")
        words = words.replace(" ", "")
        result += len(words)
    return result


def solve_018():
    result = 0
    data = []
    with open("Input/p067_triangle.txt") as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            cells = line.split(" ")
            intCells = []
            for c in cells:
                intCells.append(int(c))
            data.append(intCells)
    result = findHighestPathValue(data)
    return result


def solve_019():
    result = 0
    monthData = []
    for year in range(1901, 2001):
        for m in range(1, 13):
            monthData.append(getNumberOfDaysInMonth(m, year))

    rem = 2  # Jan 1901 starts on a Tuesday, so initial rem is 2
    for mon in monthData:
        rem += mon
        rem = rem % 7
        if rem == 0:
            result += 1

    return result


def solve_020():
    result = 0
    bigNumber = math.factorial(100)
    # print(bigNumber)
    bigString = str(bigNumber)
    for c in bigString:
        result += int(c)
    return result
# endregion


# region Problems 21-30
def solve_021():
    result = 0
    divSumList = {}
    amicableList = []
    for i in range(1, 10001):
        divSum = getSumOfProperDivisors(i)
        divSumList[i] = divSum

    for currentKey in divSumList:
        currentValue = divSumList[currentKey]
        possibleMatch = 0 if not divSumList.__contains__(currentValue) else divSumList[currentValue]
        if currentKey != currentValue and currentKey == possibleMatch:
            amicableList.append(currentKey)

    # print(amicableList)
    result = sum(amicableList)
    return result


def solve_022():
    result = 0
    data = []
    with open("Input/p022_names.txt") as inputFile:
        lines = [line.replace('"', '') for line in inputFile]
        names = lines[0].split(",")
        for name in names:
            data.append(name)
    data.sort()
    i = 1
    for d in data:
        val = getWordValue(d.lower())
        result += (val * i)
        i += 1
    return result
# endregion
