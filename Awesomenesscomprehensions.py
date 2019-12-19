#Awesomeness
#Store five names in a list. Make a second list that adds the phrase "is awesome!" to each name, using a list comprehension.
#Print out the awesome version of the names.

names =['sachin','rohit','klrahul','kohli','ashwin']

great_names=[name.title() + " the great!" for name in names]

for great_name in great_names:
    print(great_name)