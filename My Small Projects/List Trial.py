from functools import reduce

p = ['lol','Psyche','berry','hacker','apple','deth','Noice']
p.sort(key = str.lower,reverse = True)
print(p)

from random import * 

messages = ['no u','noob','fail','ha','lmao','you will die']
response = messages[randint(0,len(messages))]
print(response)

nums = [18,24,31,47,58,66,75,81,90,98,64,4231,453,5,33]

evens = list(filter(lambda x:x%2 == 0,nums))
print(evens)

total = reduce(lambda z,y:y+z,nums)
print(total)
