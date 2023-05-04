def func(string):
    l = list(string.split(","))
    return l
str = "Hello,World,How,are,you"
list = func(str)
for i in list:
    f = open("file.txt","a")
    f.write(i)
    f.close()
    
print(list)
