import os
import deniLib as dl
path = os.getcwd() + "\\"
name = "caesarTest.txt"

ct = dl.openFile(path, name)[0]
print(ct)
dl.printList([i + "\n" for i in dl.bruteForce(ct)])