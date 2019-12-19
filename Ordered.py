#Ordered Working List

#Print the list in alphabetical order.
#Print the list in its original order.
#Print the list in reverse alphabetical order.
#Print the list in its original order.
#Print the list in the reverse order from what it started.
#Print the list in its original order



#Start with the list you created in Working List.
workinglists=['ABCD','DCSX','XSED','BAXD','DSSQ']

#You are going to print out the list in a number of different orders.
#You are going to print out the list in a number of different orders.
#Print a message each time telling us what order we should see the list in.
workinglists.sort()
for wl in workinglists:
    print('sort order \t :'  + wl)

workinglists.sort(reverse=True)
for wl1 in workinglists:
    print('reverse sort order \t :' + wl1)

#Print the list in its original order.
ch=['chennai','delhi','kkdi','usa','abc']

for wl2 in sorted(ch):
    print(wl2)

for wl2 in sorted(ch, reverse=True):
    print(wl2)


print(ch)

#Permanently sort the list in alphabetical order, and then print it out.
#Permanently sort the list in reverse alphabetical order, and then print it out.
ch.reverse()
print(ch)

ch.reverse(False)
print(ch)