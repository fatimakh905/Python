"""n=100
for x in range(1,10,2):
    print(x)
    if(x==99):
        print("hehe")


list=[]

print("Enter the elemenets of list:")
for i in range(1,6):
    elements=int(input())
    list.append(elements)
print(list)


list.sort()
print("Ascending order:")
print(list)
print("Descending order:")
list.sort(reverse=True)
print(list)

maxterm=max(list)
print(f"{maxterm} is the maximum number in the list")

minterm=min(list)
print(f"{minterm} is the minimum number in the list")

print(f"{len(list)} is the number of elements in the list")

print(f"{sum(list)}")

sum=list[1]+list[2]
print(sum)
Word="Hello World"
print(Word[::3])"""

word='the'
count=0
with open("File.txt","r") as f:
   allLines=f.readlines()
   for line in allLines:
      words= line.lower().split()
      count += words.count(word)
      
print(f"The word is in the text for {count} times")