#    indentation

num=int(input("Enter a number:"))

if num>10:
    print(f"{num} is greater than ten")
    
# VAriables in python

a=10

name="fatima"

# there is no command for declaring variables in python.


# Casting

# if we want to specify type of variable .

c=str(3)    # x will be '3'
d=int(4)
e=float(6)   #z will be 6.0
b=int(7)


# Get the type of variable

v='9'

print("V is of tpye",type(v))

# Case-Sensitive
# String variables can be declared either by using single or double quotes:

p = "John"
# is the same as

P= 'John'


# Multiple values

x,y=3,"Fatima"

X=Y=10

# Unpacking a collection like list,tuple

fruits=["apple","banana","cherry","BlueBerry"]
x,y,z,k=fruits
#print(f"{x}\n{y}")

print(x,y)

# All the values in the list should be unpacked otherwise it will give an error

# Global and local variable

m="Rude"

def access():
    global m    #To make local variable global use global keyword
    m="ego"
    print(m)

access()
print(m)









