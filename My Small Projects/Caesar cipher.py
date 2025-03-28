def Cipher():
    print('This is an Encryption Program')
    print('To use this program you need a key of your choice for encryption')
    input('To start using this program press enter')

    alphabet = 'qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    
    NewMessage = ''

    print('Please write a message to be encrypted:' )
    Message = input()
    print('Choose a key:', )
    key = input()
    
    for char in Message:
        if char in alphabet:
            position = alphabet.find(char)
            newposition = (int(position) + int(key))%52
            newcharacter = alphabet[newposition]
            NewMessage += newcharacter
        else:
            NewMessage += char

    print('\nThis is the encrypted message:')
    print(NewMessage)

while True:
    Cipher()
    again = input("Would you like to use this program again?\n")
    if again.lower() == 'no':
        break

print('Thanks for using this program.Press enter to close')
input()
exit()




