import sys
data = ""
ind = -1
def encoder(letter):
    if ord(letter) + int(sys.argv[1]) > 90:
        return chr(ord(letter) + int(sys.argv[1]) - (26 * (int(sys.argv[1])//26))).upper()
    else:
        return chr(ord(letter) +int(sys.argv[1])).upper()
for line in sys.stdin:
    raw = line
    break
for character in raw:
    if character.isalpha(): data += character.upper()
for letter in data:
    ind += 1
    encode = encoder(letter)
    if ind == 50:
        print("")
        ind = 0
        print(encode, end="")
    elif ind % 5 == 0 and ind != 0:
        print(" ", end="")
        print(encode, end="")
    else: print(encode, end="")