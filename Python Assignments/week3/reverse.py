def reverse():
    s = ['a', 'b', 'c', 'd','e']
    
    print('The original list is ', s)
    i = 0
    while i != ((len(s) // 2)):
        t = s[len(s) - 1 - i]
        r = s[i]
        s[i], s[len(s) - 1 - i] = t , r
        i += 1
    print('The reversed list is ', s)


if __name__ == "__main__":
    reverse()