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