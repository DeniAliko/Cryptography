import string

def generateCodewordDict(codeword):
    uniqueCharCodeword = ""
    for char in codeword:
        if char not in uniqueCharCodeword:
            uniqueCharCodeword += char
    cipherAlphabet = [char.upper() for char in uniqueCharCodeword]

    changedAlphabet = string.ascii_uppercase[string.ascii_lowercase.find(codeword[-1]):] + string.ascii_uppercase[:string.ascii_lowercase.find(codeword[-1])]

    for char in changedAlphabet:
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
ct = masc(pt, generateCodewordDict(codeword))
print(ct)
print(masc(ct, reverseDict(generateCodewordDict(codeword))).lower())