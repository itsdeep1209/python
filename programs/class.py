#one of the popular approaches of programming is by creating objects , this is known as OOP. Python is an OOP language one of the key objectives of using classes is to reusable code
#a class is like a blueprint for creating objects , an object is an instantiation of class , in more simple words object is a collection of variables and functions
# that act on the provided data in the class Note : whenever an object calls its method , the object itself is passed as the first argument , for example we have used
# self but we can name this parameter anything as we like , 
# constructors in python : class function that begin with double underscore __ are called special functions out of which the most used one is __init__()
#function , All classes that have a function called __init__() , which is always executed when the class is being initiated.

class mysimpleclass:
    x = 20
    def printvalueofx(self):
        print("value of x is", self.x)
c = mysimpleclass()
c.printvalueofx()