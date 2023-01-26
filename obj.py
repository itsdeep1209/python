class Obj:
    pass
o = Obj()
o.id = 1
o.name = "Guido"
print(o.id , o.name)

def display():
    print(self.id , self.name)
    
o.print = display
o.print()