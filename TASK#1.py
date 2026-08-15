""" Task 2: input and output file
Date:3-6-2024
Developer name:Kaneez Fatima"""

                                                                                    
'''method 1 to take input'''


print("What is your name")    
name=input()

print(f"Hello {name}!")


"""this indicates that string is a f string inside it {name} is a placeholder 
which gets replaced by the vlue of variable during execution.
used for string formatting
it does the same thing likw when we use + but it is more readable and
automatically converts  non-string variables into string.
if we do not use f string it will be like that
print("hello"+name+"!")



method 2 to take input
the input function returns string if we want some other kind of input like age
then we will explicitly declare its data type to get input like that

age=int(input("What is your age?")) """

knowledge=input("Do you know python?\n")

print("Thanks for answering my question",name)


import os                   
"""module for intercation with operating system
    python standard library
    The os module has defferent functions and features like os,chdir(path)
    ,os.listdir(path='.') any many more.

"""

print("The current working directory is" ,os.getcwd())


'''whenwe use + in the print function it means the strng and variable join 
together and there is no space .When we , it will provide a space between
string and variable.
for single line comments use #

'''

'''indentation means whitesapce at the start of the lines for defining structure
,functions,loops etc'''



#  To run any file directly write its path in command line like that
#   %run C:/Users/lenovo/.spyder-py3/task2.py