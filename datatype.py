#1.bool
isMarried = True
print("isMarried", isMarried , type(isMarried))

#2. int
count = 5
print("count" , count , type (count))

#3 float
pi = 3.1415
print("pi" , pi , type(pi))

#4 complex
complex = 1.2j
print("complex", complex , type(complex))

#5 str
name = "Guid"
print("name",name, type(name))

#6 list (linked list but can be used as array)
days = ["Mon", "Tue" , "Wed", "Thu" , "Fri" , "Sat" , "Sun"]
print("days", days, type(days))
print(days[3])
record = [123, "Guid" , 66.3 , True]
record[0] = 456
print(record)

#7 tuple - fixed and read only list
tuple = (123, "guido" , 66.3 , True)
print(tuple[0])
print("tuple", tuple, type(tuple))

#8 sets unique value
lottery = {123, 234, 123 , 456 , 123}
print("lottery", lottery, type(lottery))

#9 dictionary(map or hastable) - key:value
person = {"id":1, "name":"Guido"}
print("person", person , type(person))