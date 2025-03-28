name = input('What is your name?')
print('Hello', name, '.Welcome to trivia')
choice = input('Which option do you want to choose(history/football)')
 
score = 0


if choice == 'football':
    ans = input('Are you ready?(yes/no)')
     
    if ans.lower() == 'yes':
        ans1 = input('Which country has the most world cups?')
        if ans1.lower() == 'brazil':
            score += 1
            print('correct')
        else:
            print('Incorrect, the correct answer is brazil')
            

        ans2 = input('Who won the champions league 2019?')
        if ans2.lower() == 'liverpool':
            score += 1
            print('correct')
        else:
            print('Incorrect, the correct answer is liverpool')

        ans3 = input('Who is the first goalkeeper to get a balon d\'or?')
        if ans3.lower() == 'lev yashin':
            score += 1
            print('correct')
        else:
            print('Incorrect, the correct answer is lev yashin')

        ans4 = input('Who is the highest goal scorer in all time epl?')
        if ans4.lower() == 'alan shearer':
            score += 1
            print('correct')
        else:
            print('Incorrect, the correct answer is Alan Shearer')

        mark = (score/4)*100
        print('Thank you for playing!')
        print('Your score is', score)
        if mark > 50:
            print('You got', mark,'% so Very Noice')
        else:
            print('You got', mark,'% so you\'re a dumbass')
        
    else:
        print('ok then.Die!!')

elif choice == 'history':
     ans = input('Are you ready?(yes/no)')
     
     if ans.lower() == 'yes':
        ans1 = input('?')
        if ans1.lower() == '':
            score += 1
            print('correct')
        else:
            print('Incorrect, the correct answer is brazil')
            

        ans2 = input('?')
        if ans2.lower() == '':
            score += 1
            print('correct')
        else:
            print('Incorrect, the correct answer is liverpool')

        ans3 = input('?')
        if ans3.lower() == '':
            score += 1
            print('correct')
        else:
            print('Incorrect, the correct answer is lev yashin')

        ans4 = input('?')
        if ans4.lower() == '':
            score += 1
            print('correct')
        else:
            print('Incorrect, the correct answer is Alan Shearer')

        mark = (score/4)*100
        print('Thank you for playing!')
        print('Your score is', score)
        if mark > 50:
            print('You got', mark,'% so Very Noice')
        else:
            print('You got', mark,'% so you\'re dumb')
    

q = input('Do you want to play another quiz?')
if q.lower() == 'no':
    print('Noice decision')
else:
    print('Well too bad.No other quiz for you')

print('Goodbye')
       

