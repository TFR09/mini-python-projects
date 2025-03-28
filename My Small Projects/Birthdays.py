Birthdays = {'trevor':'Feb 22','giles':'Nov 18','ken':'Oct 29','kevin':'Sep 16','george':'July 30','timothy':'July 20'}

while True:
    print('Please enter name to get their birthday,(Blank to end program)')
    name = input()
    if name == '':
        break
    else:
        if name.lower() in Birthdays:
            print(name,"'s birthday is on",Birthdays[name])
        elif name not in Birthdays:
            print('I don\'t have the birthday for', name,'Please enter person\'s birthday')
            birthday = input()
            Birthdays[name.lower] = birthday
            input('Database updated. Press enter to exit')
            
