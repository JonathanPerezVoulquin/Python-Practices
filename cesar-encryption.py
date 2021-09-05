alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
message = "This is an encrypted message"
encrypted = ""
key = 7                                                 #this is the number of characters to be advanced in the alphabet

for l in message.upper():
    if l in alphabet:
        index = alphabet.find(l)                      #index of the letter #method of string .find()
        index += key                                  # index number that will replace it
        if index >= 27:
            index -= 27                               #if it is a greater than or equal, we subtracter 27 so as not to exceed the index of the alphabet
        encrypted += alphabet[index]
    else:
        encrypted += l

print(encrypted)

print("------------------------o---------------------------")

#DECRYPT MESSAGE
alphabet2 = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
encrypted2 = "AÑOZ OZ HT LTJYFWALK SLZZHNL"
massage_decrypt = ""

for l in encrypted2.upper():
    if l in alphabet:
        index = alphabet2.find(l)
        index -= key
        if index < 0:
            index += 27
        massage_decrypt += alphabet2[index]
    else:
        massage_decrypt += l
print(massage_decrypt)