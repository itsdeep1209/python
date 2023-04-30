#write a program to identify if string is palindrome
# def palindrome(s):
#     if s == s[::-1]:
#         print("string is palindrome")
#     else:
#         print("string is not palindrome")
# word = input("Enter the word to check palindrome")
# palindrome(word)

#write a program to identify lcm of two numbers

def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm 

num1 = input("ENter first number")
num2 = input("Enter second number")

print("the lcm of" , int(num1) , "and" , int(num2) , "is", lcm(int(num1),int(num2)))
            


