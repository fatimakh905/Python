countries={
    "Afghanistan":" Kabul",
    "Srilanka":" Colombo",
    "India":"    New Dehli"
 }

# Print  all items
#x=countries.items()
#print(x) 

countries.update({"China":"Beijing"})

for x,y in countries.items():
    print(x,y)

print(countries["India"])