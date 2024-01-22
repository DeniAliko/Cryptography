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

pt = input("Plain text: ")
print(shift(pt.replace(" ", "").lower(), int(input("Shift: "))))

def unShift(ct, n):
    return shift(ct.lower(), (-1) * n).lower()

ct = input("Cipher text: ")
print(unShift(ct.replace(" ", "").lower(), int(input("Shift: "))))