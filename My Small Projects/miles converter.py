# km = 1.6 * miles
print('Welcome to this program that can convert miles to kms or vice versa')

def convert_m(miles):
    x = miles * 1.6
    if x != 1:
        print(x, 'kms')
    else:
        print(x, 'km')

def convert_km(km):
    x = km / 1.6
    if x != 1:
        print(x, 'miles')
    else:
        print(x, 'mile')

print('Do you want to convert miles to kms or kms to miles?')
function = input()
print('please input the value you want to convert')
value = int(input())
try:
    if function.lower() == 'miles to kms':
        convert_m(value)
    elif function.lower() == 'kms to miles':
        convert_km(value)
    input()
except Exception:
    print('You have not entered a number')
    print('please input the value you want to convert')
    value = int(input())
    try:
        if function.lower() == 'miles to kms':
            convert_m(value)
        elif function.lower() == 'kms to miles':
            convert_km(value)
        input()
    except Exception:
        print('You have not entered a number for the second time.Are you autistic? Goodbye!')
        input()
