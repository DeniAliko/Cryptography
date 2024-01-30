def openFile(path, fileName):
    with open(path + fileName, mode = "r") as f:
        output = [i.strip() for i in f.readlines()]

    return output

def printList(list):
    for item in list:
        print(item)

def bruteForce(ct):
    output = []
    cipher = ct.upper()
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