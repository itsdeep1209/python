#python has the inbuilt os module which provides us with many useful methods/functions to work with directories, subdirectories and files as well.
#get current working directory
import os
print(os.getcwd())

#change directory
import os
os.chdir("/var/")
print(os.getcwd())

#list diretories and files
import os
print(os.listdir())

#create new directory
import os
os.mkdir("mydir")