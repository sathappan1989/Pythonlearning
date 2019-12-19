#Store the first ten letters of the alphabet in a list.
#Use a slice to print out the first three letters of the alphabet.
#Use a slice to print out any three letters from the middle of your list.
#Use a slice to print out the letters from any point in the middle of your list, to the end.

letters=['a','b','c','d','e','f','g','h','i','j']

first_three=letters[0:3]

for user in first_three:
    print(user.title())

middle_three=letters[3:7]

for user in middle_three:
    print(user.title())

last_three=letters[7:]

for user in last_three:
    print(user.title())

print(letters)