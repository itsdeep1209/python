def hello():
    print("Hello")

hello()

def print_natural(start,stop=10,increment=1):
    while start < stop:
        print(start,end='')
        start += increment
    print()
print_natural(20,30)
print("Hello")

def dragons_ahead(my_list=[]):
    my_list.append(5)
    print(my_list)
dragons_ahead()



def sum_all(message1, message2, *args):
    total = 0
    for value in var_args:
        total += value
    return total

result = sum_all("my list", "new list" ,1 ,2 , 3, 4 ,5, 6, 7,8 )
print(result)

def var_args(*args):
    print(args)

var_args(1, "Guido" , 66.3)

