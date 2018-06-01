alphabet = 'abcdefghijklmnopqrstuvwxyz'
numerics = '`~1!2@3#4$5%6^7&8*9(0)-_=+'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = 6
newMessage = ''

message = input('Please enter a message: ')

for character in message:
    #lower case letters
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = numerics[newPosition] + alphabet[newPosition] 
        newMessage += newCharacter
    #upper case letters
    elif character in ALPHABET:
        position = ALPHABET.find(character)
        newPosition = (position + key) % 26
        newCharacter = numerics[newPosition] + ALPHABET[newPosition] 
        newMessage += newCharacter
    #other characters
    else:
        newMessage += character

print(newMessage)
