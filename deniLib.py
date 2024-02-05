# MISC:
def openFile(path, fileName):
    with open(path + fileName, mode = "r") as f:
        output = [i.strip() for i in f.readlines()]

    return output

def writeFile(path, fileName, text):
    with open(path + fileName, mode = "w") as f:
        f.write(text)

def keepLowercaseLetters(text):
    output = ""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    for char in text.lower():
        if char in lowercase:
            output += char

    return output

def printList(list):
    for item in list:
        print(item)

# FREQUENCY ANALYSIS:

def letterFrequency(text):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    counts = {}
    for char in lowercase:
        counts[char] = 0

    for char in text.lower():
        if char in counts.keys():
            counts[char] += 1

    totalCount = 0
    for char in counts.keys():
        totalCount += counts[char]

    output = {}
    for char in counts.keys():
        output[char] = round((counts[char] / totalCount), 2)

    return output

def digraphFrequency(text, displayNum):
    frequencies = {}
    for i in range(0, len(text) - 1):
        if text[i] + text[i+1] not in frequencies:
            frequencies[text[i] + text[i+1]] = 1
        else:
            frequencies[text[i] + text[i+1]] += 1

    orgFrequencies = sorted(frequencies.items(), key=lambda x:x[1], reverse=True)
    output = {}
    for i in range(0, displayNum):
        output[orgFrequencies[i][0]] = orgFrequencies[i][1]

    return output

def trigraphFrequency(text, displayNum):
    frequencies = {}
    for i in range(0, len(text) - 2):
        if text[i] + text[i+1] + text[i+2] not in frequencies:
            frequencies[text[i] + text[i+1] + text[i+2]] = 1
        else:
            frequencies[text[i] + text[i+1] + text[i+2]] += 1

    orgFrequencies = sorted(frequencies.items(), key=lambda x:x[1], reverse=True)
    output = {}
    for i in range(0, displayNum):
        output[orgFrequencies[i][0]] = orgFrequencies[i][1]

    return output

# MASC CIPHERS:
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