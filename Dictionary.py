countries={
    "Afghanistan":" Kabul",
    "Srilanka":" Colombo",
    "India":"    New Dehli"
 }

# Print  all items
#x=countries.items()
#print(x) 
#   update(change or add) countries.update({"Canada":"Texas"})


for x,y in countries.items():
    print(x,y)
    
new_country=input("\nEnter a new country:")
new_capital=input("Enter the capital of country:")

countries.update({new_country:new_capital})

print("\nUpdated Ditionary:\n\t")
for x,y in countries.items():
    print(x,y)

"""
Remove last item
countries.popitem()
Remove any item
countries.pop("India")
del countries("India")
Remove all items
del countries
print(countries)"""

    
""" To  add new item in dictionary

countries["Pakistan"]="Islamabad"
print(countries)"""

""" to get all values
x=countries.values()
print(x)

This method will return all the keys in the dictionary
x=countries.keys()
print(x)"""

"""x=countries["India"]
print(x)
print(countries["Afghanistan"])"""


# dict constructor
# thisdict=dict(name = "ayesha", age=11 , Study = "6th")