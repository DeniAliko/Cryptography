# MISC:

def openFile(filePath, fileName):
    '''Get a list of the lines of a file'''
    with open(filePath + fileName, mode = "r") as f:
        output = [i.strip() for i in f.readlines()]

    return output

def writeFile(filePath, fileName, textToWrite):
    '''Write text to a file'''
    with open(filePath + fileName, mode = "w") as f:
        f.write(textToWrite)

def keepLowercaseLetters(text):
    '''Take only the letters in a text and make them lowercase'''
    output = ""
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    for char in text.lower():
        if char in lowercase:
            output += char

    return output

def printList(list):
    '''Print each item in a list on its own line'''
    for item in list:
        print(item)

def generateShiftDict(cipherLetter):
    '''Pick a cipherLetter to map to the letter a in the plaintext'''
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerList = [char for char in lowercase]
    upperList = [char for char in uppercase]

    # Reorganize the two lists to match the key and plainletter
    upperStart = upperList.index(cipherLetter)
    upperList = upperList[upperStart:] + upperList[:upperStart]

    # build the dictionary
    output = {}
    for i in range(len(lowerList)):
        output[lowerList[i]] = upperList[i]

    return output

def reverseDict(dictionary):
    '''Reverses the values of a dictionary assuming a 1 to 1 mapping'''
    output = {}
    for char in dictionary.keys():
        output[dictionary[char]] = char
    return output

def indexOfCoincidence(text):
    '''Returns the index of coincidence of a certain text'''
    possibleChars = {char for char in text.lower()}
    ic = 0
    for char in possibleChars:
        if text.lower().count(char) > 1:
            num1 = text.lower().count(char)
            num2 = text.lower().count(char) - 1
            den1 = len(text)
            den2 = len(text) - 1
            if den2 == 0:
                continue
            ic += (num1 / den1) * (num2 / den2)
    return ic

def averageListValues(list):
    '''Get the average of values in a list'''
    sum = 0
    for val in list:
        sum += val
    return sum / len(list)

def chiSquare(observed, expected):
    '''Returns the chi-square test value of two lists (list values are numerical)'''
    if len(observed) != len(expected):
        pass
    chi = 0
    for i in range(len(observed)):
        chi += (observed[i] - expected[i])**2 / (expected[i])

    return chi

# TRANSPOSITION CIPHERS

def railFence(plainText, rowNum):
    '''Encrypt using the railfence cipher'''
    table = [["" for j in range(len(plainText))] for i in range(rowNum)]
    walkerCoord = [0, 0]
    down = True
    for charindex in range(len(plainText)):
        table[walkerCoord[1]][walkerCoord[0]] = plainText[charindex]
        if walkerCoord[1] == rowNum - 1 and down:
            down = not down
        elif walkerCoord[1] == 0 and not down:
            down = not down

        if walkerCoord[0] < len(plainText) - 1:
            walkerCoord[0] += 1
        else:
            break
        if down:
            walkerCoord[1] += 1
        else:
            walkerCoord[1] -= 1

    output = ""
    for i in range(rowNum):
        for j in range(len(plainText)):
            output += table[i][j]

    return output

def railFenceDecrypt(cipherText, rowNum):
    '''Takes a railfence encrypted string and a given number of rows and decrypts it'''
    # Make the table:
    table = [["" for j in range(len(text))] for i in range(rowNum)]
    # Define the 'walker'
    walkerCoord = [0, 0]
    down = True
    # iterate through each column:
    for charindex in range(len(cipherText)):
        # along the zigzag, place placeholder "*"
        table[walkerCoord[1]][walkerCoord[0]] = "*"
        # Define what happens when the zigzag pattern hits the top or the bottom of the table
        if walkerCoord[1] == rowNum - 1 and down:
            down = not down
        elif walkerCoord[1] == 0 and not down:
            down = not down

        # actually changing the walker's coordinates:
        if walkerCoord[0] < len(text) - 1:
            walkerCoord[0] += 1
        else:
            break
        if down:
            walkerCoord[1] += 1
        else:
            walkerCoord[1] -= 1

    # by ROW (not by column) place the letters of the encrypted text on the placeholders
    for row in table:
        for i in range(len(row)):
            if row[i] == "*":
                row[i] = text[0]
                text = text[1:]

    # read column by column to reconstruct the decrypted text
    output = ""
    for i in range(len(table[0])):
        for row in table:
            if row[i] != "":
                output += row[i]

    return output

# FREQUENCY ANALYSIS:

def letterFrequency(text):
    '''Dictionary of letters and their frequencies'''
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
        output[char] = (counts[char] / totalCount)

    return output

def digraphFrequency(text, displayNum):
    '''List of most frequent digraphs'''
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
    '''List of most frequent trigraphs'''
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

def caesarBruteForce(cipherText):
    '''List of all 26 possible caesar cipher shifts'''
    output = []
    cipher = cipherText.upper()
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

def generateCodewordDict(codeword):
    '''Generate a substitution dictionary using a codeword'''
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

def masc(plainText, substitutionDict):
    '''Substitutes every letter in a plaintext with a substitution dictionary'''
    output = ""
    for char in plainText:
        if char in substitutionDict.keys():
            output += substitutionDict.get(char, "[NOT FOUND]")
    return output

# PASC CIPHERS:

def vigenereEncrypt(pt, codeword):
    '''Vigenere cipher encrypt'''
    codeword = keepLowercaseLetters(codeword.lower())
    output = ""
    for i in range(len(pt)):
        output += generateShiftDict(codeword[i % len(codeword)].upper())[pt[i]]

    return output

def vigenereDecrypt(ct, codeword):
    '''Vigenere cipher decrypt'''
    codeword = keepLowercaseLetters(codeword.lower())
    output = ""
    for i in range(len(ct)):
        output += reverseDict(generateShiftDict(codeword[i % len(codeword)].upper()))[ct[i]]

    return output

def autokeyEncrypt(pt, codeword):
    '''Vigenere autokey cipher encryption'''
    codeword = keepLowercaseLetters(codeword.lower()) + keepLowercaseLetters(pt.lower())
    output = ""
    for i in range(len(pt)):
        output += generateShiftDict(codeword[i % len(codeword)].upper())[pt[i]]

    return output

def autokeyDecrypt(ct, codeword):
    '''Vigenere autokey cipher decryption'''
    codeword = keepLowercaseLetters(codeword.lower())
    output = ""
    for i in range(len(ct)):
        newPtLetter = reverseDict(generateShiftDict(codeword[i % len(codeword)].upper()))[ct[i]]
        output += newPtLetter
        codeword += newPtLetter

    return output

def guessVigenereCodewordLength(ct, maxCheckLength):
    '''Use Index of Coincidence to predict the codeword length of a Vigenere cipher'''
    englishIC = indexOfCoincidence("".join([(key * int({'a':8.04, 'b':1.48, 'c':3.34, 'd':3.82, 'e':12.49, 'f':2.40,'g':1.87, 'h':5.05, 'i':7.57, 'j':0.16, 'k':0.54, 'l':4.07, 'm':2.51,'n':7.23, 'o':7.64, 'p':2.14, 'q':0.12, 'r':6.28, 's':6.51, 't':9.28,'u':2.73, 'v':1.05, 'w':1.68, 'x':0.23, 'y':1.66, 'z':0.09}[key] * 100)) for key in {'a':8.04, 'b':1.48, 'c':3.34, 'd':3.82, 'e':12.49, 'f':2.40,'g':1.87, 'h':5.05, 'i':7.57, 'j':0.16, 'k':0.54, 'l':4.07, 'm':2.51,'n':7.23, 'o':7.64, 'p':2.14, 'q':0.12, 'r':6.28, 's':6.51, 't':9.28,'u':2.73, 'v':1.05, 'w':1.68, 'x':0.23, 'y':1.66, 'z':0.09}.keys()]))
    guess = 0
    keylengthIC = {guess: 2}
    for n in range(2, maxCheckLength + 1):
        mascs = ["" for i in range(n)]
        for i in range(len(ct)):
            mascs[i % n] += ct[i]
        keylengthIC[n] = averageListValues([indexOfCoincidence(substring) for substring in mascs])
    for key in keylengthIC.keys():
        if abs(keylengthIC[key] - englishIC) < abs(keylengthIC[guess] - englishIC):
            guess = key
    return guess

def statisticalCrackVigenere(ct, maxKeylength=10):
    '''Use chi-squared test to guess likely letter shifts for each masc in a vigenere cipher'''
    keylength = guessVigenereCodewordLength(ct, maxKeylength)
    mascs = ["" for i in range(keylength)]
    for i in range(len(ct)):
        mascs[i % keylength] += ct[i]
    
    for substring in mascs:
        letterFrequencyDict = letterFrequency(substring)
        englishFrequencyDict = {'a':8.04, 'b':1.48, 'c':3.34, 'd':3.82, 'e':12.49, 'f':2.40,'g':1.87, 'h':5.05, 'i':7.57, 'j':0.16, 'k':0.54, 'l':4.07, 'm':2.51,'n':7.23, 'o':7.64, 'p':2.14, 'q':0.12, 'r':6.28, 's':6.51, 't':9.28,'u':2.73, 'v':1.05, 'w':1.68, 'x':0.23, 'y':1.66, 'z':0.09}
        shiftStats = {}
        for i in range(26):
            shiftStats[i] = chiSquare([], [])