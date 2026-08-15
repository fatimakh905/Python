""" Task : List operations
Date:5-6-2024
Developer name:Kaneez Fatima"""

numberofelements=5

list=[]

for i in range(numberofelements):
    element=int(input("Enter numbers for the list\n"))
    list.append(element)
    
    
print(list)


list.sort()
print("Ascending order:")
print(list)

maxval=max(list)
print("\nMaximum value in list=",maxval)


minval=min(list)
print("\nMinimum value in list=",minval)

total=sum(list)
print("\nSum of all elements in the list=",total)

length=len(list)
print("\nLength of the list=",length)

print("Average=",total/length)

