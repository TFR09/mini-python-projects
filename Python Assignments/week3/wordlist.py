def words():
    list = []
    while True: 
        words = []
        command = input("Enter command: ")
        if (command == 'quit'):
        break
        words = command.split()
        add = (words[0] == 'add')
        if add:
        list.append(words[1])
        
        find = (words[0] == 'find')
        if find:
        for i in range(len(list)):
            if words[1] in list[i]:
            print(list[i])


if __name__ =="__main__":
    words()