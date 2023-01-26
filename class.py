class Person:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def display(self):
        print(self.id , self.name)
        
p = Person(1,"Guido")
p.display()