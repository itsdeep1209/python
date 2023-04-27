print("This is a program to discuss on data types in Python")
a = 123
b = 122
print("Multiplication of a and b is",  a * b)

print("lets talk about strings")

a = 'Hello'
b = 'world'

print("Concatenation of string a and b is", a + b)

S = 'spam'
S.find('pa')
print (S[0])
print (S.find('am'))
s = 'A\nB\tc'
print(s)

print("List are positionally ordered collections of aribitrarily typed objects")

l = [123 , 'spam' , 1.23]
print("list is" , l)
print(l[1:])

for i in l:
    print(i)

print("Python dictionaries are not sequences like string instead they are mappings. Mappings are also collections of different objects but they store objects by key instead of relative positions")

D = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}

print(D)

print("sets are essentially like a valueless dictonaries , because they are unordered , unique and immutable , items are stored only once in set")
S = {1,2,3,4}
print(type(S))