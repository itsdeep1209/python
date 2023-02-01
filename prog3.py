# a is a pointer and 1 is an object(expression)

a = 1
print(a)

class Person:
    '''
    class:Person
    params: id (number), name(str)
    '''

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_person(self):
        '''
        method: print
        args: none
        remarks: prints id and name
        '''
        print(self.id, self.name)

def add_sub(a,b):
    for key , value in locals().items():
        print(key,value)
    return a+b, a-b

for key,value in globals().copy().items():
    print(key, value)

x,y = add_sub(5, 7)
print(x, y)

a, b = 1,2
print(a, b)

a, b = b, a
print(a, b)