# Your name: Deni
# In-class Alberti Cipher assignment - 02/15/2024
# Rename this file by replacing <YourFirstName> with your first name.
# You are allowed to re-use function(s) that you have already created in this class.
# e.g. generating dictionaries or doing substitution with a dictionary.

import random
import deniLib as dl

stabilis = 'ABCDEFGILMNOPQRSTVXZ1234'
mobilis  = '&moebkxihcnzurypagqldfts'

def genD(key,plainletter):
    '''generates the dictionary of substitutions when a given key faces a plainletter'''
    # for example, the key 'k' faces the plainletter 'A'

    # Establish the stabilis and mobilis
    stabList = [char for char in stabilis]
    mobList = [char for char in mobilis]

    # Reorganize the two lists to match the key and plainletter
    stabStart = stabList.index(plainletter)
    mobStart = mobList.index(key)
    stabList = stabList[stabStart:] + stabList[:stabStart]
    mobList = mobList[mobStart:] + mobList[:mobStart]

    # build the dictionary
    output = {}
    for i in range(len(stabList)):
        output[stabList[i]] = mobList[i]

    return output

def cleanup(text):
    text = text.replace('U', '1')
    text = text.replace('W', '2')
    text = text.replace('J', '321')
    text = text.replace('Y', '3')
    text = text.replace('H', '4')
    text = text.replace('K', '123')
    out = ''
    for char in text:
        if char in stabilis:
            out += char
    return out

def unCleanUp(text):
    text = text.replace('123', 'K')
    text = text.replace('321', 'J')
    text = text.replace('1', 'U')
    text = text.replace('2', 'W')
    text = text.replace('3', 'Y')
    text = text.replace('4', 'H')
    
    out = ''
    for char in text:
        out += char
    return out

def albertiEncode(pt, k):
    ''' encodes a plaintext with the Alberti cipher and a given key '''
    output = "A"
    subDict = genD(k, "A")
    subCount = 0
    targetCount = random.randint(1, 10)
    # iterate through each letter in the plantext, substituting with whatever the current dictionary is
    for i in range(len(pt)):
        if subCount == 5:
            # after a randomly chosen amount of substitutions, change the dictionary
            newLetter = stabilis[random.randint(0, len(stabilis) - 1)]
            subDict = genD("k", newLetter)
            output += newLetter
            subCount = 0
            targetCount = random.randint(1, 10)
        output += subDict[pt[i]]
        subCount += 1
        
    return output

def albertiDecode(ct, k):
    currentDict = genD(k, ct[0])
    output = ""
    for i in range(len(ct)):
        if ct[i] in stabilis:
            currentDict = genD(k, ct[i])
            continue
        output += dl.reverseDict(currentDict)[ct[i]]

    return output

def main():
    gate = input("Encode [E] or decode [D]: ")
    k = input("Enter your keyletter: ")
    pt = input("Enter your plaintext (all CAPS): ")
    if gate == "E":
        print(albertiEncode(cleanup(pt.upper()), k))
    elif gate == "D":
        print(unCleanUp(albertiDecode(pt, k).upper()))

main()