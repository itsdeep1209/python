#python has several functions for creating  , reading , updating and deleting files. Python uses open() function to open a file and has the following modes:
# "r": Read - Default value , opens a file for reading , error if the file does not exist.
# "a": Append: Opens a file for appending , creates the file if it does not exist.
# "w": Write: opens a file for writing , creates the file if it does not exists.
# "x": Create : creates the specified file , returns an error if the file exists.
#"t": Text: default value , text mode
# "b": Binary: binary mode

f = open("sample_file.txt", "r")
print(f.read())
f.close()

#loop through the lines

f = open("sample_file.txt", "r")
for x in f:
    print("line:" , x)
f.close()

# read the file if file exists

import os
if os.path.exists("sample_file.txt"):
  f = open("sample_file.txt", "r")
  print(f.read())
  f.close()
else:
   print("file not exist")

#append mode
f = open("sample_file.txt","a")
f.write("this is a line added by python function\n")
f.close()

