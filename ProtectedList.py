#Your goal in this exercise is to prove that copying a list protects the original list.
#Make a list with three people's names in it.
#Use a slice to make a copy of the entire list.
#Add at least two new names to the new copy of the list.
#Make a loop that prints out all of the names in the original list, along with a message that this is the original list.
#Make a loop that prints out all of the names in the copied list, along with a message that this is the copied list.

names = ['sachin','rohit','sehwag']

name = names[:]

name.append('viru')
name.append('dhoni')

for name1 in names:
    print(name1.title())

for name2 in name:
    print(name2.upper())
