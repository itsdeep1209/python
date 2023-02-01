import sys
import dis

class Person:
    '''
    class: Person
    params: id(number) , name(str)
    '''

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def print_person(self):
        '''
        method: print
        args: none
        remarks: prints id and name
        '''
        print(self.id, self.name)

    def __del__(self):
        print(self.id, self.name, "was deleted")


p = Person(1,"Guido")
q = p
print(type(p), id(p), sys.getrefcount(p))
del q
print(type(p), id(10), sys.getrefcount(1026743) )

def add(a,b):
    c = a + b
    return c

dis.dis(add)