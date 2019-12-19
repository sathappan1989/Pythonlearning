#First List
#Store the values 'python', 'c', and 'java' in a list. Print each of these values out, using their position in the list.

languages = ['python','c','java']
print(languages)

language1 = languages[0]
language2= languages[1]
language3 = languages[2]

print(language1.title())
print(language2.title())
print(language3.title())

for language4 in languages:
    print("A nice programming language is value, " + language4.title() + "!")