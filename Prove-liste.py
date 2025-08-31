primi = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
match = 11

for el in primi:
    if el == match:
        output = str(el) + " == " + str(match)
        print("Match! " + output)
    else:
        print(el)