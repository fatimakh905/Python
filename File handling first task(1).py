
"""Reading a file content
f=open("Test file.txt","r")
text=f.read()
print(len(text))

f.close()

#Writing in a file which does not exist at first

f=open("file.txt","w")
text=f.write("Hello! Its me")
print(text)
f.close()

# this will print the number of characters returned by write method.It means
 # that there is no use of variable when writing in a file .You have to read 
 # the file first after writing in it to print its content.

f=open("file.txt","a")
f.write("I am learning python")
f.close()"""
 
# Another method if we do not want to close the file again and again
with open("File.txt","r") as f:
  con=f.read()
  text=con.split()
print(len(text))

count=0
word='the'
with open("File.txt","r") as f:
    lines=f.readlines()
for line in lines:
    words=line.lower().split()
    count +=words.count(word)
print(f"Total 'the' word in python:{count}")


    




