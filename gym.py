#A gymnast can earn a score between 1 and 10 from each judge; nothing lower, nothing higher.
# All scores are integer values; there are no decimal scores from a single judge.
#Store the possible scores a gymnast can earn from one judge in a tuple.

##Print out the sentence, "The lowest possible score is ___, and the highest possible score is ___." Use the values from your tuple.

#Print out a series of sentences, "A judge can give a gymnast _ points."

#Don't worry if your first sentence reads "A judge can give a gymnast 1 points."

#However, you get 1000 bonus internet points if you can use a for loop, and have correct grammar. hint


number=[5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

print("The lowest possible score is %d, and the highest possible score is %d" % ( number[0] , number[-1]) )

for judge in number:
    print("A judge can give a gymnast %d points" % judge )

