import os
import deniLib as dl
path = os.getcwd() + "\\"
name = "caesarTest.txt"

ct = dl.openFile(path, name)[0]
dl.printList([i + "\n" for i in dl.bruteForce(ct)])

name = "codewordTest.txt"
ct = dl.openFile(path, name)[0]
codePhrase = "marcuscicero"
encryptDict = dl.generateCodewordDict(codePhrase)
decryptDict = dl.reverseDict(encryptDict)
print(dl.masc(ct, decryptDict))