""" Task: Print fibonacci sequence
Date:5-6-2024
Developer name:Kaneez Fatima"""


limit=int(input("Enter the number of terms upto which fibonacci sequence is printed\n"))

number1=0
number2=1
for i in range(number1,limit):
     print(number1)
     next=number1+number2
     number1=number2
     number2=next
     
     
     