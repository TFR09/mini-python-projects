list=[]

size = input('how many names do you want in this list?')

for i in range(int(size)):
    x = input('enter a name')
    list.append(x)

def name_length():
    short_name = 0
    long_name = 0
    for name in list:
        if len(name)>5:
            long_name+=1
        else:
            short_name+=1

    print('There are', short_name,'short names and', long_name,'long names')

name_length()
                
