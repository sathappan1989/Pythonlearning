#Ordered Numbers
#Make a list of 5 numbers, in a random order.
#You are going to print out the list in a number of different orders.
#Each time you print the list, use a for loop rather than printing the raw list.
#Print a message each time telling us what order we should see the list in.
#Print the numbers in the original order.
#Print the numbers in increasing order.
#Print the numbers in the original order.
#Print the numbers in decreasing order.
#Print the numbers in their original order.
#Print the numbers in the reverse order from how they started.
#Print the numbers in the original order.
#Permanently sort the numbers in increasing order, and then print them out.
#Permanently sort the numbers in descreasing order, and then print them out.

nos=['4','5','2','1','99']

#Print the numbers in the original order.
for no in nos:
    print(no)

#Print the numbers in increasing order.
nos.sort()
for no1 in nos:
    print('Increasing order ' + no1)

print(nos)


nos.sort(reverse=True)
for no2 in nos:
    print('original ' + no2)