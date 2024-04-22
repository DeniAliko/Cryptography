def slideList(inputList):
    '''Take the first entry in a list and slide it to the end'''
    return inputList[1:] + [inputList[0]]

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