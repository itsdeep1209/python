actual = 25

guess = 0
while guess < actual:
    guess += 1
print("actual" , guess)

# zero -> false
# Non zero -> true
# a = 3
# b = 5
value = a > b 
print("value" , value)
if True:
    print("when true")
else:
    print("when false")

# for (i=0 , i<10 , i+=1)
languages = ['c' , 'c++' , 'python' , 'java']
for language in languages:
    print(language)

#number = [1,2,3,4,5,6,7,8,9]
for value in range(1, 101 , 2):
    print(value , end=" ")