itemslist = ["Apple", "Banana", "Milk"]
for item in itemslist:
    print item

print

#andere Moeglichkeit

for i in range(len(itemslist)):
    print itemslist[i],

print

# mit while Schleife

i = len(itemslist)
while i > 0:
    i -= 1
print itemslist[i],