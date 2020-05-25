
string = input("Enter a word: ")
lenght = len(string)
newString = ""
decryptedStr = ""

for i in range(lenght):
    newString = newString + chr(ord(string[i]) + 5)

print(newString)

for i in range(lenght):
    decryptedStr = decryptedStr + chr(ord(newString[i]) - 5)

print(decryptedStr)