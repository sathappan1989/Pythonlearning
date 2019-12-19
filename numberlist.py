# Store the first million numbers in a list.
numbers = list(range(1,1000001))

# Show the length of the list:
print("The list 'numbers' has " + str(len(numbers)) + " numbers in it.")

# Show the last ten numbers:
print("\nThe last ten numbers in the list are:")
for number in numbers[-10:]:
    print(number)