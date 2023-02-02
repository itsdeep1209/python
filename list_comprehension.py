list2 = [ i for i in range(1,6)]
print(list2)

#ternary operator -> (condition) ? truevalue: falsevalue
is_done = False
value = 0
if is_done:
    value = 1
else:
    value = 2
print(value)

value = [1 if is_done else 2]
print(value)