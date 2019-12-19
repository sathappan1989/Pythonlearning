#Working Backwards¶
#Write out the following code without using a list comprehension:
#plus_thirteen = [number + 13 for number in range(1,11)]

numbers=[]

for number in range(1,10):
    numbers.append(number+13)

for number in numbers:
    print(number)

##Numerical comprehensions
numbers=[number+13 for number in range(1,11)]

for num in numbers:
    print(num)