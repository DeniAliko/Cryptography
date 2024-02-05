import os
import deniLib as dl
path = os.getcwd() + "\\"
name = "testText.txt"

test = dl.openFile(path, name)[0]
print(dl.letterFrequency(test))
print(dl.digraphFrequency(test, 10))
print(dl.trigraphFrequency(test, 10))