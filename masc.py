import string
def shift(pt, n):
    # encrypts plain text (pt, all lowercase no whitespace) using a caesar cipher with shift n
    encrypted = ""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    for char in pt:
        letterIndex = lower.find(char)
        encrypted += upper[(letterIndex + n) % 26]

    return encrypted

def unShift(ct, n):
    return shift(ct.lower(), (-1) * n).lower()

pt = input("Plain text: ")
print(shift(pt.replace(" ", "").lower(), int(input("Shift: "))))
ct = input("Cipher text: ")
print(unShift(ct.replace(" ", "").lower(), int(input("Shift: "))))

def getCaesarDict(n):
    shiftDict = {}
    for i in range(len(string.ascii_lowercase)):
        shiftDict[string.ascii_lowercase[i]] = string.ascii_uppercase[(i+n)%26]
    return shiftDict

def dictEncrypt(pt, n):
    ct = ""
    for char in pt:
        ct += getCaesarDict(n)[char]
    return ct

def dictDecrypt(ct, n):
    return dictEncrypt(ct.lower(), (-1) * n).lower()

pt = input("Plain text: ")
print(dictEncrypt(pt.replace(" ", "").lower(), int(input("Shift: "))))
ct = input("Cipher text: ")
print(dictDecrypt(ct.replace(" ", "").lower(), int(input("Shift: "))))