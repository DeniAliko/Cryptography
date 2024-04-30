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

def slideList(inputList):
    '''Take the first entry in a list and slide it to the end'''
    return inputList[1:] + [inputList[0]]

def sieveOfEratosthenes(number):
    '''Return primes smaller than or equal to a given number'''
    prime = [True for i in range(number+1)]
    primeCheck = 2
    while primeCheck ** 2 <= number:
        if prime[primeCheck] == True:
            for i in range(primeCheck ** 2, number + 1, primeCheck):
                prime[i] = False
        primeCheck += 1
    output = []
    for i in range(2, number+1):
        if prime[i]:
            output.append(i)
    return output

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
            output += substitutionDict[char]
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

def crackVigenere(ct, returnKeyword = False, maxKeylength=10):
    '''Use chi-squared test to guess likely letter shifts for each masc in a Vigenere Cipher'''
    # Create a list of the substring MASCs that make up the Vigenere Cipher
    keylength = guessVigenereCodewordLength(ct, maxKeylength)
    mascs = ["" for i in range(keylength)]
    likelyShifts = []
    crackedMascs = []
    for i in range(len(ct)):
        mascs[i % keylength] += ct[i]
    
    # Individually break each substring using chi-squared test and frequency analysis
    for substring in mascs:
        letterFrequencyDict = letterFrequency(substring)
        englishFrequencyDict = {'a':8.04, 'b':1.48, 'c':3.34, 'd':3.82, 'e':12.49, 'f':2.40,'g':1.87, 'h':5.05, 'i':7.57, 'j':0.16, 'k':0.54, 'l':4.07, 'm':2.51,'n':7.23, 'o':7.64, 'p':2.14, 'q':0.12, 'r':6.28, 's':6.51, 't':9.28,'u':2.73, 'v':1.05, 'w':1.68, 'x':0.23, 'y':1.66, 'z':0.09}
        likelyShift = 0
        likeleyChiSquare = 99999999999999999999999

        # Generate the most likely shift value using chi-squared test by iterating through all possible shift values
        for i in range(26):
            # test the given shift value
            shiftedLetterFrequencyDict = {}
            for j in range(i, 26):
                shiftedLetterFrequencyDict[list(letterFrequencyDict.keys())[j]] = letterFrequencyDict[list(letterFrequencyDict.keys())[j]]
            for j in range(i):
                shiftedLetterFrequencyDict[list(letterFrequencyDict.keys())[j]] = letterFrequencyDict[list(letterFrequencyDict.keys())[j]]

            # do the chi-squared test and see if the value is lower than the previous lowest value
            testChiSquare = chiSquare([shiftedLetterFrequencyDict[key] for key in shiftedLetterFrequencyDict.keys()], [englishFrequencyDict[key] for key in englishFrequencyDict.keys()])
            if testChiSquare < likeleyChiSquare:
                likelyShift = i
                likeleyChiSquare = testChiSquare

        # use the most likely shift value to decode the given substring
        crackedMascs.append(masc(substring, reverseDict(generateShiftDict("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[likelyShift]))))
        likelyShifts.append(likelyShift)

    # re-weave the deciphered substrings together to form a deciphered output
    output = ""
    for i in range(len(crackedMascs[1])):
        for j in range(len(crackedMascs)):
            if i + 1 <= len(crackedMascs[j]):
                output += crackedMascs[j][i]
    # if asked for by the user, returns the keyword used in the vigenere cipher
    if returnKeyword:
        twoOut = [output, ""]
        for shift in likelyShifts:
            twoOut[1] += "ABCDEFGHIJKLMNOPQRSTUVEXYZ"[shift]

        return twoOut

    return output

# Enigma

def rotateRotor(rotor):
    '''See slideList'''
    return slideList(rotor)

def rotorForwards(letter, rotor):
    '''Take a letter (Capital character) and a rotor list (rI, rII, rIII) and translate the letter forwards through the rotor'''
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return alphabet[(alphabet.find(letter) + rotor[alphabet.find(letter)]) % 26]

def rotorBackwards(letter, rotor):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for index in range(len(alphabet)):
        if alphabet[(index + rotor[index]) % 26] == letter:
            return alphabet[index]

def generatePlugboard():
    '''Generate a plugboard dictionary based on user inputs'''
    settings = input('List the plugboard connections (formatted like "AB CD EF GH"): ') + " "
    plugboard = {}
    cacheString = ""
    for i in range(len(settings)):
        if settings[i] != " ":
            cacheString += settings[i]
        if settings[i] == " " and cacheString != "":
            plugboard[cacheString[0]] = cacheString[1]
            plugboard[cacheString[1]] = cacheString[0]
            cacheString = ""
    return plugboard

def generateRotorSettings():
    '''Generate a rotor initialization list based on user inputs'''
    settings = input('List the initial rotor settings (formatted slow, medium, fast, "4 21 13"): ') + " "
    rotorInit = []
    cacheString = ""
    for i in range(len(settings)):
        if settings[i] != " ":
            cacheString += settings[i]
        if settings[i] == " " and cacheString != "":
            rotorInit.append(int(cacheString))
            cacheString = ""
    return rotorInit

def reflect(letter, reflector):
    '''Runs a letter through a given reflector (mapping dictionary)'''
    return reflector[letter]

def enigmaTransform():
    '''Transforms an all-caps text using the enigma machine'''

    # ROTOR AND REFLECTOR MAPPING INITIALIZATION
    if True:
        rotorIII = [1, 2, 3, 4, 5, 6, 22, 8, 9, 10, 13, 10, 13, \
            0, 10, 15, 18, 5, 14, 7, 16, 17, 24, 21, 18, 15]

        rotorII =  [0, 8, 1, 7, 14, 3, 11, 13, 15, 18, 1, 22, 10, \
                6, 24, 13, 0, 15, 7, 20, 21, 3, 9, 24, 16, 5]

        rotorI =   [4, 9, 10, 2, 7, 1, 23, 9, 13, 16, 3, 8, 2, \
                9, 10, 18, 7, 3, 0, 22, 6, 13, 5, 20, 4, 10]

        reflector = {'A':'Y', 'B':'R', 'C':'U', 'D':'H', 'E':'Q', 'F':'S', \
                'G':'L', 'H':'D', 'I':'P', 'J':'X', 'K':'N', 'L':'G', \
                'M':'O', 'N':'K', 'O':'M', 'P':'I', 'Q':'E', 'R':'B', 'S':'F', \
                'T':'Z', 'U':'C', 'V':'W', 'W':'V', 'X':'J', 'Y':'A', 'Z':'T' }
        # Fast: rotorIII
        # Medium: rotorII
        # Slow: rotor1
        # Reflector: reflector
    
    # ROTOR AND PLUGBOARD INITIALIZATION:
    if True:
        rotorStates = generateRotorSettings()
        plugboardSettings = generatePlugboard()
        plainText = input("Input text here: ")

        # Set rotor III:
        for i in range(rotorStates[2]):
            rotorIII = rotateRotor(rotorIII)

        # Set rotor II:
        for i in range(rotorStates[1]):
            rotorII = rotateRotor(rotorII)

        # Set rotor I:
        for i in range(rotorStates[0]):
            rotorI = rotateRotor(rotorI)

    output = ""

    for letter in plainText:
        # ROTATE ROTORS
        if True:
            rotorIII = rotateRotor(rotorIII)
            rotorStates[2] = (rotorStates[2] + 1) % 26
            if rotorStates[2] == 22:
                rotorII = rotateRotor(rotorII)
                rotorStates[1] = (rotorStates[1] + 1) % 26
                if rotorStates[1] == 4:
                    rotorI = rotateRotor(rotorI)
                    rotorStates[0] = (rotorStates[0] + 1) % 26
                    rotorII = rotateRotor(rotorII)
                    rotorStates[1] = (rotorStates[1] + 1) % 26

        # SUBSTITUTE
        if True:
            if letter in plugboardSettings.keys():
                letter1 = plugboardSettings[letter]
            else:
                letter1 = letter
            letter2 = rotorForwards(letter1, rotorIII)
            letter3 = rotorForwards(letter2, rotorII)
            letter4 = rotorForwards(letter3, rotorI)
            letter5 = reflect(letter4, reflector)
            letter6 = rotorBackwards(letter5, rotorI)
            letter7 = rotorBackwards(letter6, rotorII)
            letter8 = rotorBackwards(letter7, rotorIII)
            if letter8 in plugboardSettings.keys():
                letter9 = plugboardSettings[letter8]
            else:
                letter9 = letter8

            output += letter9

    return output

# VERNAM CIPHER

def ITA2Encode(text, returnWithSpaces = False):
    '''Encodes a text into binary using the ITA2 Mapping'''
    text = text.lower()
    ITA2_ltr = {"e":1, "\n":2, "a":3, " ":4, "s":5, "i":6, "u":7, "d":9, "r":10, "j":11, \
            "n":12, "f":13, "c":14, "k":15, "t":16, "z":17, "l":18, "w":19, "h":20, \
            "y":21, "p":22, "q":23, "o":24, "b":25, "g":26, "m":28, "x":29, "v":30}
    ITA2_fig = {"@":0, "3":1, "-":3, "'":5, "8":6, "7":7, "4":10, \
                ",":12, "!":13, ":":14, "(":15, "5":16, "+":17, ")":18, "2":19, "$":20, \
                "6":21, "0":22, "1":23, "9":24, "?":25, "&":26, ".":28, "/":29, ";":30}
    LTRS = 31
    FIGS = 27
    output = ""
    letter = True

    if text[0] in ITA2_ltr.keys():
        output += format(LTRS, 'b')
        letter = True
        output += " "
    elif text[0] in ITA2_fig.keys():
        output += format(FIGS, 'b')
        letter = False
        output += " "

    for char in text:
        if char in ITA2_ltr.keys() and not letter:
            output += format(LTRS, 'b')
            letter = True
            output += " "
        elif char in ITA2_fig.keys() and letter:
            output += format(FIGS, 'b')
            letter = False
            output += " "

        if letter:
            output += format(ITA2_ltr[char], 'b')
        if not letter:
            output += format(ITA2_fig[char], 'b')

        output += " "
    
    leadingZeroOutput = ""
    cacheString = ""
    for i in range(0, len(output)):
        if output[i] != " ":
            cacheString += output[i]
        if output[i] == " ":
            if len(cacheString) != 5:
                cacheString = "0" * (5 - len(cacheString)) + cacheString

            leadingZeroOutput += cacheString
            if returnWithSpaces:
                leadingZeroOutput += " "
            cacheString = ""

    return leadingZeroOutput

def vernamTransform(text, key):
    '''Use the Vernam transform to encrypt/decrypt a binary message'''
    output = ""
    for i in range(0, len(text)):
        if text[i] == key[i]:
            output += "1"
        else:
            output += "0"
    return output

def ITA2Decode(text):
    '''Decode an ITA2 binary message back into text'''
    ITA2_ltr = {"e":1, "\n":2, "a":3, " ":4, "s":5, "i":6, "u":7, "d":9, "r":10, "j":11, \
        "n":12, "f":13, "c":14, "k":15, "t":16, "z":17, "l":18, "w":19, "h":20, \
        "y":21, "p":22, "q":23, "o":24, "b":25, "g":26, "m":28, "x":29, "v":30}
    ITA2_fig = {"@":0, "3":1, "-":3, "'":5, "8":6, "7":7, "4":10, \
                ",":12, "!":13, ":":14, "(":15, "5":16, "+":17, ")":18, "2":19, "$":20, \
                "6":21, "0":22, "1":23, "9":24, "?":25, "&":26, ".":28, "/":29, ";":30}
    ITA2_ltr = reverseDict(ITA2_ltr)
    ITA2_fig = reverseDict(ITA2_fig)
    LTRS = 31
    FIGS = 27

    output = ""
    for i in range(0, len(text), 5):
        cacheString = "0b" + text[i:i+5]
        number = int(cacheString, 2)
        if number == 31:
            activeDict = ITA2_ltr
            continue
        if number == 27:
            activeDict = ITA2_fig
            continue

        output += activeDict[number]
        cacheString = ""

    return output

# RSA

def isGenerator(generator, key):
    '''Check if a given generator is actually a generator for a given key'''
    output = True
    moduluses = []
    for i in range(0, key - 1):
        moduluses.append((generator**i) % key)
    return len(moduluses) == len(set(moduluses))

def findGenerator(key):
    '''Finds the smallest generator number for a given key (slow)'''
    primesUpTo = sieveOfEratosthenes(key)
    i = 0
    while True:
        if isGenerator(primesUpTo[i], key):
            return primesUpTo[i]
        else:
            i += 1
