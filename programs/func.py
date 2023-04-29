#A function is a block of code that only runs when it is called , we can pass data known as parameters into a function and function can return data as a result
#In python we define function using def keyword
# we can call a function by function name followed by paranthesis
#passing arguments: information data can be passed into functions as arguments and arguments can be named arguments inside the paranthesis spearated by comma
#we can use return statement to get value back from function

def sum(a,b):
    return a + b
sumvalue = sum(4,5)
print("sum is", sumvalue)

# Lamnbda function : In python the functions which doesnt have a defined name is called anonymous function, In python anonymous function are defined using lambda keyword
# and a lambda function can take any number of arguments but can only have one expression.

sum = lambda a,b:a + b
print(sum(12,13))

# a function can call itself is called recursive function.
def factorial(x):
    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))
num=4
factorial_num = factorial(num)
print("Factorial of num", num , "is", factorial_num)
