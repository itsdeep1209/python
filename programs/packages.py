#what is a package in python: the package in python in a simple sense is a directory with python files and a file with the name __init__.py. This means 
#that every directory inside of a python path which contains a file named __init__.py , will be treated as package by python, A python package can have
#subpackage and modules its a well organized hierarchy of directories for easier access.

#import module from package

import Greetings.student.greet
Greetings.student.greet.say_hello()

#import package as alias

import Greetings.student.greet as greet_student
greet_student.say_hello()

# import module without package prefix

from Greetings.student import greet
greet.say_hello()

# import only function from package mofule

from Greetings.student.greet import say_hello
say_hello()