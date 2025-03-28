import sys

passwords = ['swordfish','clownfish','octopus','squid','lmao']

while True:
    print('What is your name?')
    name = input()
    if name.upper() != 'TREVOR':
        continue
    print('What is the password?')
    password = input()
    if password.lower() in passwords:
        break
    else:
        print('Acess Denied.Try again')
print ('Access Granted')

exit()

