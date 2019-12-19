#Famous People
#Make a list that includes the names of four famous people
#Remove each person from the list, one at a time, using each of the four methods we have just seen:
#Pop the last item from the list, and pop any item except the last item.
#Remove one item by its position, and one item by its value.
#Print out a message that there are no famous people left in your list, and print your list to prove that it is empty.

famous = ['sachin','kohli','dhoni','rohit']

last_ppl=famous.pop()
print(last_ppl)


first_ppl=famous.pop(0)
print(first_ppl)


del famous[-1]


famous.remove('kohli')
print(famous)