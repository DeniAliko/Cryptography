# 1:
def firstLast2(string):
    '''Return a string comprised of the first two and the last two characters in input string'''
    if len(string) >= 2:
        return string[0] + string[1] + string[-2] + string[-1]
    return ""

print(firstLast2("w3resource"))

# 2:
def cashReplace(string):
    '''replaces every other instance of the letter in the first index with $'''
    firstChar = string[0]
    output = ""
    for char in string[1:]:
        if char == firstChar:
            output += "$"
        else:
            output += char
    return firstChar + output

print(cashReplace("restart"))

# 3:
def giveSuffix(string):
    '''adds "ing" or "ly" to strings longer than length 3'''
    if len(string) >= 3:
        if string[-3:] == "ing":
            return string + "ly"
        else:
            return string + "ing"
    return string

print(giveSuffix("abc"))
print(giveSuffix("string"))

# 4:
def longestStr(list):
    '''finds the longest string in a list and returns it and its length'''
    stringList = list.copy()
    organized = []
    done = False
    currentLength = 0
    while not done:
        if len(stringList) == 0:
            done = True
        for string in stringList:
            if len(string) == currentLength:
                organized.append([string, currentLength])
                stringList.remove(string)
        currentLength += 1
    return organized[-1]

print(longestStr(["asdf", "fontaine", "cryptography", "weewee", "airplane"]))

# 5:
def findUSA(string):
    '''find occurences of "usa" ignoring capitalization'''
    count = 0
    for i in range(len(string)-2):
        focus = string[i] + string[i+1] + string[i+2]
        if focus.lower() == "usa":
            count += 1
    return count

print(findUSA("USA? Inexcusable crusaders by the thousands!"))