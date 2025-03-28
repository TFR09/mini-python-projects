from random import choice

def main():
    while True:
        ans = input('Here is a password generator. Press any key to start the program or enter q to quit.').lower()
        if ans == 'q':
            print('Goodbye!')
            break
        generate_password(get_length)
    


def get_length():
    return input('How long do you want your password to be?')

def generate_password(length):
    chars = '1234567890qwertyuiopasdfghjklzxvbnmQWERTYUIOPASDFGHJKLZXCVBNM?&%$#@!*^(){}[]'

    password = ''
    for _ in range(int(length)):
        password += choice(chars)
    return f"Your password is {password}\n"

if __name__ == '__main__': 
    main() 
