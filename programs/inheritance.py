#what is inheritance in python: we can define a new class with little

#define a parent class

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greetPerson(self):
        print("Hello", self.name)

#child/derived class

class Patient(Person):
    def __init__(self, name, age, case):
        Person.__init__(self, name, age)
        self.case = case
    def print_case(self):
        print("patient case is ",self.case)

patientObject = Patient("John", 30 ,"cold")
patientObject.greetPerson()
patientObject.print_case()

#using super function

# def Patient(Person):
#     def __init__(self, name, age, case):
#         super().__init__(name,age)

# newParent = Patient("Jon")
# newParent.greetPerson()