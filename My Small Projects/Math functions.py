#for each parameter the x is the number of values to be printed in the sequence

def fibonacci(x):
    a=int(input('Enter the first number of your sequence'))
    b=int(input('Enter the second number of your sequence'))

    sequence = []
    sequence.append(a)
    sequence.append(b)
    if x==0:
        print(a)
    elif x<0:
        print('Invalid number. Please enter a number above zero')
    else:
        for i in range(2,x):
            c = a+b
            a = b
            b = c
            sequence.append(c)
    l = input('Do you want your sequence in list form?(yes or no)')
    if l.lower() == 'yes':    
        print(sequence)
    else:
        for i in sequence:
            print(i)
    
def factorial(x):
    ans = 1
    if x < 0:
        print('Invalid')
    elif x == 0:
        print(1)    
    else:
        for _ in range(x+1):
            ans *= x
            x-=1
            if x == 0:
                break
            else:
                continue
        print(ans)

def geometric(a,b,x):
    nums = input('Do you want your sequence in list form?(y/n)')

    sequence = []
    sequence.append(a)
    for i in range(1,x):
        a*= b
        sequence.append(a)

    if nums.lower() == 'y':    
        print(sequence)
    else:
        for i in sequence:
            print(i)

def collatz(x):
    if x%2 == 0:
        return x//2        
    else:
        return 3*x+1
  
def Collatz():
    number = input('Enter any number ')
    try:
        while number != 1:
            number = collatz(int(number))
            print(number)
    except ValueError:
        print('Error.Please enter a number')

Collatz()

def check_prime(x):
    for i in range(2,x):
        if x%i == 0:
            return "Not Prime"
    return "Prime"
        
    
