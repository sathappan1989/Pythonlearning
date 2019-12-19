#Five Wallets¶
#Imagine five wallets with different amounts of cash in them. Store these five values in a list, and print out the following sentences:
#"The fattest wallet has $ value in it."
#"The skinniest wallet has $ value in it."
#"All together, these wallets have $ value in them."

wallet=[100,200,300,400,501]
fattest=max(wallet)
skinniest=max(wallet)
together=sum(wallet)

print("The fattest wallet has $" + str(fattest) +" value in it.")
print("The skinniest wallet has $" + str(skinniest) + " value in it.")
print("All together, these wallets have $" + str(together) + " value in them.")