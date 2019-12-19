#Make a list that includes four careers, such as 'programmer' and 'truck driver'.
carrers=['programmer','tester','cloud','truck driver']

#Use the list.index() function to find the index of one career in your list.
print(carrers.index('tester'))

#Use the in function to show that this career is in your list.
print ('cloud' in carrers)

#Use the append() function to add a new career to your list.
carrers.append('python')
for carrer in carrers:
    print(carrer)

#Use the insert() function to add a new career at the beginning of the list.
carrers.insert(4,'bpm')
print(carrers)

#Use a loop to show all the careers in your list.
for test in carrers:
    print(test)