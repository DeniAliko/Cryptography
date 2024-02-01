import deniLib as dl
import os
path = os.getcwd() + "\\"
name = "secretMessageForFontaine.txt"

codeword = "linearalgebra"
encryptDict = dl.generateCodewordDict(codeword)
inputText = dl.keepLowercaseLetters(input("plainText: "))
encrypted = dl.masc(inputText, encryptDict)

dl.writeFile(path, name, encrypted)