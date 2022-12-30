def hello_world():
    return "Hello World"
print(hello_world())
c = 'a' + 'b'
print (c)

name = input("what's your name")
# remove whitespace from str
name = name.strip()
# capitalize user's name
name = name.capitalize()
#capitalize first letter of each word
name = name.title()
#remove whitespace from str and capitalize users name
name = name.strip().title()
print("hello" , name)
print(f"hello , {name}")
# split users name into first name and last name
# first,last = name.split("")
print (f"hello, {name}")