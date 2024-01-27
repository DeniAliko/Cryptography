import string

def generateCodeDict(codeword):
    uniqueCharCodeword = ""
    for char in codeword:
        if char not in uniqueCharCodeword:
            uniqueCharCodeword += char
    cipherAlphabet = [char.upper() for char in uniqueCharCodeword]
    for char in string.ascii_uppercase:
        if char not in cipherAlphabet:
            cipherAlphabet.append(char)

    output = {}
    for i in range(26):
        output[string.ascii_lowercase[i]] = cipherAlphabet[i]

    return output

def reverseDict(dictionary):
    output = {}
    for char in dictionary.keys():
        output[dictionary[char]] = char
    print(output)
    return output

def masc(text, subD):
    output = ""
    for char in text:
        if char in subD.keys():
            output += subD.get(char, '\U0001F4A9')
    return output

pt = input("Plain text: ")
codeword = input("Codeword: ")
ct = masc(pt, generateCodeDict(codeword))
print(ct)
print(masc(ct, reverseDict(generateCodeDict(codeword))).lower())