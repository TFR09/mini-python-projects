def bmi():
    print('Please enter your weight in kgs')
    weight = int(input())
    print('Please enter your height in cms')
    height = int(input())
    
    if height == 0:
        print("N/A")
    else:
        bmi = weight / ((height / 100)**2)
        print('Your BMI is: ',bmi)


if __name__ == "__main__":
    bmi()