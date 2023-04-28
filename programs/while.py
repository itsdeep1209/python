#the while loop we can iterate and execute a set of statements as long as an expression is true
# break statement can stop the loop even if the while condition is true 
# continue statement can stop the current iteration and continue with next
#else in while loop can run a block of code once when the condition is no longer true

i=0
while i<10:
    print(i)
    i += 1
else:
    print("i is no longer less than 10")
