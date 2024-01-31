def openFile(path, fileName):
    with open(path + fileName, mode = "r") as f:
        output = [i.strip() for i in f.readlines()]

    return output

def printList(list):
    for item in list:
        print(item)

def bruteForce(ct):
    output = []
    cipher = ct.upper()
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(1, 26):
        shiftDict = {}
        for j in range(len(lowercase)):
            shiftDict[uppercase[j]] = lowercase[(j+i)%26]

        decode = ""
        for char in cipher:
            decode += shiftDict[char]
        output.append(decode)
    return output

def reverseDict(dictionary):
    output = {}
    for char in dictionary.keys():
        output[dictionary[char]] = char
    return output

def generateCodewordDict(codeword):
    uniqueCharCodeword = ""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in codeword:
        if char not in uniqueCharCodeword:
            uniqueCharCodeword += char
    cipherAlphabet = [char.upper() for char in uniqueCharCodeword]

    changedAlphabet = uppercase[lowercase.find(codeword[-1]):] + uppercase[:lowercase.find(codeword[-1])]

    for char in changedAlphabet:
        if char not in cipherAlphabet:
            cipherAlphabet.append(char)

    output = {}
    for i in range(26):
        output[lowercase[i]] = cipherAlphabet[i]

    return output

def masc(text, subD):
    output = ""
    for char in text:
        if char in subD.keys():
            output += subD.get(char, "[NOT FOUND]")
    return output