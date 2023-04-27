colors = ['White','Red','Blue']
for x in colors:
    print (x)

# break statement can stop  the loop before it has looped through all the items.
colors = ["White","Green","Blue"]
for x in colors:
    if (x == "Green"):
        break
    print(x)

# continue statement can stop the current iteration of the loop and continue with the next
colors = ["White","Green","Blue"]
for x in colors:
    if (x == "Green"):
        continue
    print(x)

# To loop through a set of code specified number of times , we can use range() function it starts from 0
for x in range(10):
    print(x)

# for loop support optional else block , else keyword in a for loop specifies a block of code to be executed when the loop is finished.
colors = ['White','Red','Blue']
for x in colors:
    print (x)
else:
    print("All items processed")
