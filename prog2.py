# printf formatted
# %d -> decimal
# %s - string
# %f - flaoting point
# %05d %-5d
# %20s %20s
# %6.2f

id = 10
name = "Guido"
age = 66.3

print("[%05d] [%20s] [%5.2f]" % (id, name, age))

print("[{0:^20}".format(name))

# - and = -> < and > and ^
print("id=[{2:>05d}] name=[{0:^20.3s}] age=[{1:6.2f}]".format(name,age,id))
print( f"id=[{id:>05d}] name=[{name:^20.3s}] age=[{age+10:6.2f}] {2+3}")