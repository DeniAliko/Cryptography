def railFenceDecrypt(text, rowNum):
    '''Takes a railfence encrypted string and a given number of rows and decrypts it'''
    # Make the table:
    table = [["" for j in range(len(text))] for i in range(rowNum)]
    # Define the 'walker'
    walkerCoord = [0, 0]
    down = True
    # iterate through each column:
    for charindex in range(len(text)):
        # along the zigzag, place placeholder "*"
        table[walkerCoord[1]][walkerCoord[0]] = "*"
        # Define what happens when the zigzag pattern hits the top or the bottom of the table
        if walkerCoord[1] == rowNum - 1 and down:
            down = not down
        elif walkerCoord[1] == 0 and not down:
            down = not down

        # actually changing the walker's coordinates:
        if walkerCoord[0] < len(text) - 1:
            walkerCoord[0] += 1
        else:
            break
        if down:
            walkerCoord[1] += 1
        else:
            walkerCoord[1] -= 1

    # by ROW (not by column) place the letters of the encrypted text on the placeholders
    for row in table:
        for i in range(len(row)):
            if row[i] == "*":
                row[i] = text[0]
                text = text[1:]

    # read column by column to reconstruct the decrypted text
    output = ""
    for i in range(len(table[0])):
        for row in table:
            if row[i] != "":
                output += row[i]

    return output