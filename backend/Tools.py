import math
import enum


class Months(enum.IntEnum):
    Jan = 1
    Feb = 2
    Mar = 3
    Apr = 4
    May = 5
    Jun = 6
    Jul = 7
    Aug = 8
    Sep = 9
    Oct = 10
    Nov = 11
    Dec = 12


_abc = {'a': 1,
       'b': 2,
       'c': 3,
       'd': 4,
       'e': 5,
       'f': 6,
       'g': 7,
       'h': 8,
       'i': 9,
       'j': 10,
       'k': 11,
       'l': 12,
       'm': 13,
       'n': 14,
       'o': 15,
       'p': 16,
       'q': 17,
       'r': 18,
       's': 19,
       't': 20,
       'u': 21,
       'v': 22,
       'w': 23,
       'x': 24,
       'y': 25,
       'z': 26}
_collatzData = {1: 0}
_pathData = {(1, 1): 2}


def getNthFibonacciTerm(x: int):
    result = 0
    if x <= 0:
        result = 0
    elif x == 1:
        result = 1
    elif x == 2:
        result = 2
    else:
        result = getNthFibonacciTerm(x-1) + getNthFibonacciTerm(x-2)
    return result


def getNextCollatzTerm(x: int):
    result = 0
    if (x % 2) == 0:
        result = x/2
    else:
        result = 3*x + 1
    return result


def getCollatzStepCount(x):
    result = 0
    if x in _collatzData:
        result = _collatzData[x]
    else:
        nextTerm = getNextCollatzTerm(x)
        nextCount = getCollatzStepCount(nextTerm)
        _collatzData[int(x)] = int(nextCount) + 1
        result = _collatzData[x]
    return result


def getPathCount(x, y):
    result = 0
    if x <= 0 | y <= 0:
        result = 1
    elif x == 1:
        result = y + 1
    elif y == 1:
        result = x + 1
    else:
        if y > x:  # flip if y is larger to reduce duplicate values in cache
            z = y
            y = x
            x = z
        if (x, y) in _pathData:
            result = _pathData[(x, y)]
        else:
            value = getPathCount(x - 1, y) + getPathCount(x, y - 1)
            _pathData[(x, y)] = value
            result = value
    return result


def getNthTriangleTerm(x: int):
    result = 0
    for i in range(1, x+1):
        result += i
    return result


def getPrimeComponents(x: int):
    result = []
    current = x
    index = 3
    if x <= 1:
        result.append(1)
    while (current > 1) & (current % 2 == 0):
        result.append(2)
        current /= 2
    while (current > 1) & (index <= current):
        if current % index == 0:
            result.append(index)
            current /= index
        elif index > math.sqrt(current):
            result.append(int(current))
            break
        else:
            index += 2
    return result


def isPrime(x: int):
    result = False
    if x > 1:
        if x == 2 or x == 3 or x == 5 or x == 7:
            result = True
        elif x % 2 == 0:
            result = False
        else:
            index = 3
            floor = math.sqrt(x)
            while index < floor:
                if x % index == 0:
                    result = False
                    break
                else:
                    index += 2
                    if index > floor:
                        result = True
                        break
    return result


def getNthPrimeNumber(x: int):
    result = 0
    if x < 1:
        result = 0
    elif len(_listOfPrimes) >= x:
        result = _listOfPrimes[x-1]
    else:
        index = _listOfPrimes[-1]
        while len(_listOfPrimes) < x:
            index += 2
            if isPrime(index):
                _listOfPrimes.append(index)
        result = _listOfPrimes[x-1]
    return result


_listOfPrimes = [2, 3]


def getFactors(x: int):
    results = []
    components = getPrimeComponents(x)
    componentCount = len(components)
    permutationCount = math.pow(2, len(components))
    for permIndex in range(0, int(permutationCount)):
        permProduct = 1                                 # iterate though all possible permutations of components
        for compIndex in range(0, componentCount):      # pick out appropriate components via bit masking
            if permIndex & 2**compIndex:
                permProduct *= components[compIndex]
        if permProduct not in results:
            results.append(permProduct)
    return results


def isPalindrome(x):                                    # note this is case-sensitive for strings
    result = False
    inputString = str(x)
    for i in range(0, len(inputString)):
        if inputString[i] != inputString[len(inputString) - (i + 1)]:
            result = False
            break
        elif i >= (len(inputString) - (i + 1)):
            result = True
            break
    return result


# only valid for 1 -> 1000 inclusive
def toWords(x):
    result = ""
    if x == 1000:
        result = "one thousand"
    elif x > 900:
        result = "nine hundred and "
    elif x == 900:
        result = "nine hundred "
    elif x > 800:
        result = "eight hundred and "
    elif x == 800:
        result = "eight hundred "
    elif x > 700:
        result = "seven hundred and "
    elif x == 700:
        result = "seven hundred "
    elif x > 600:
        result = "six hundred and "
    elif x == 600:
        result = "six hundred "
    elif x > 500:
        result = "five hundred and "
    elif x == 500:
        result = "five hundred "
    elif x > 400:
        result = "four hundred and "
    elif x == 400:
        result = "four hundred "
    elif x > 300:
        result = "three hundred and "
    elif x == 300:
        result = "three hundred "
    elif x > 200:
        result = "two hundred and "
    elif x == 200:
        result = "two hundred "
    elif x > 100:
        result = "one hundred and "
    elif x == 100:
        result = "one hundred "

    y = x % 100
    if y > 90:
        result += "ninety-"
    elif y == 90:
        result += "ninety"
    elif y > 80:
        result += "eighty-"
    elif y == 80:
        result += "eighty"
    elif y > 70:
        result += "seventy-"
    elif y == 70:
        result += "seventy"
    elif y > 60:
        result += "sixty-"
    elif y == 60:
        result += "sixty"
    elif y > 50:
        result += "fifty-"
    elif y == 50:
        result += "fifty"
    elif y > 40:
        result += "forty-"
    elif y == 40:
        result += "forty"
    elif y > 30:
        result += "thirty-"
    elif y == 30:
        result += "thirty"
    elif y > 20:
        result += "twenty-"
    elif y == 20:
        result += "twenty"

    if 20 > y > 9:
        if y == 19:
            result += "nineteen"
        elif y == 18:
            result += "eighteen"
        elif y == 17:
            result += "seventeen"
        elif y == 16:
            result += "sixteen"
        elif y == 15:
            result += "fifteen"
        elif y == 14:
            result += "fourteen"
        elif y == 13:
            result += "thirteen"
        elif y == 12:
            result += "twelve"
        elif y == 11:
            result += "eleven"
        elif y == 10:
            result += "ten"
    else:
        z = y % 10
        if z == 9:
            result += "nine"
        elif z == 8:
            result += "eight"
        elif z == 7:
            result += "seven"
        elif z == 6:
            result += "six"
        elif z == 5:
            result += "five"
        elif z == 4:
            result += "four"
        elif z == 3:
            result += "three"
        elif z == 2:
            result += "two"
        elif z == 1:
            result += "one"

    return result


def findHighestPathValue(matrix):
    result = 0
    for i in range(1, len(matrix)):
        highRow = matrix[i-1]
        lowRow = matrix[i]
        for j in range(0, len(lowRow)):
            highCell0 = highRow[j-1] if j > 0 else 0
            highCell1 = highRow[j] if j < len(highRow) else 0
            lowRow[j] += max(highCell0, highCell1)
        result = max(lowRow)

    return result


def getNumberOfDaysInMonth(mon, year):
    result = 0
    if mon == Months.Jan:
        result = 31
    elif mon == Months.Feb:
        result = 29 if (year % 4 == 0) and (year != 1900) else 28  # only valid for 1801 -> 2099
    elif mon == Months.Mar:
        result = 31
    elif mon == Months.Apr:
        result = 30
    elif mon == Months.May:
        result = 31
    elif mon == Months.Jun:
        result = 30
    elif mon == Months.Jul:
        result = 31
    elif mon == Months.Aug:
        result = 31
    elif mon == Months.Sep:
        result = 30
    elif mon == Months.Oct:
        result = 31
    elif mon == Months.Nov:
        result = 30
    elif mon == Months.Dec:
        result = 31

    return result


def getSumOfProperDivisors(x):
    result = 0
    divs = getFactors(x)
    divs.remove(x)
    for d in divs:
        result += d

    return result


def getWordValue(x):
    result = 0
    for i in range(0, len(x)):
        result += _abc[x[i]]
    return result


