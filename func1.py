# 1.function to return sum of two numbers

def sum(a,b):
    return a + b

print(sum(78,3))


# 2. function to calculate the factorial of a number

def fact(num):
    if num == 0:
        return 1
    else:
        return  num * fact(num-1)

result = fact(5)
print("factorial of number 5 is:", result)

#3. A function that takes a list and return the maximum value

def max_value(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

result = max_value([4,3,9,8,1,4,10])

print("The maximum number is:", result)

# 4. A function that takes a two string and return a concatenated string

def concat_string(str1 , str2):
    string = str1 + str2
    return string

result = concat_string("Hello", "World")
print("The result of concatenated string is:", result)

# 5. A function that returns true if its a even number and false if its odd.

def func(num):
    return num % 2 == 0

result = func(4)
print(result)

#6. A function that takes a list of numbers and return the average

def avg(numbers):
    total = 0 
    for i in numbers:
     total = total + i
    return total/len(numbers) 

result = avg([1,2,3,4,5])
print(result)
