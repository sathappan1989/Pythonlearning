#Finding Python
#Store a sentence in a variable, making sure you use the word Python at least twice in the sentence.
##Use the in keyword to prove that the word Python is actually in the sentence.
#Use the find() function to show where the word Python first appears in the sentence.
#Use the rfind() function to show the last place Python appears in the sentence.
#Use the count() function to show how many times the word Python appears in your sentence.
#Use the split() function to break your sentence into a list of words. Print the raw list, and use a loop to print each word on its own line.
#Use the replace() function to change Python to Ruby in your sentence.

sentence='I like python and learning python'

search=sentence.find('python')
print(search)

search=sentence.rfind('python')
print(search)

search=sentence.count('python')
print(search)

words=sentence.split(" ")
print(words)

change=sentence.replace('like','love')
print(change)