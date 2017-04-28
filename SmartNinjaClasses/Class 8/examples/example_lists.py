# initialize
newList = []
print newList
print

# append single elements - neue Elemente dazuhänge oder +=
newList.append('Banana')
print newList
print

# append add multiple elements with other lists
oldList = ['Milk', 'Honey']
shoppingList = newList + oldList
print shoppingList
print

# refer to elements
print shoppingList[0]
print shoppingList[-1]
print

# refer to multiple elements
print shoppingList[:-1]            # slicen :  (bis zu einem gewissen Bereich) Stopwert nicht dabei
print shoppingList[1:]             # ab 1 bis zum Ende BSP (1:3) = 1,2 (letztes Element wird nicht geschrieben
print

# reverse
shoppingList.reverse()
print shoppingList
shoppingList.reverse()
print

# remove
shoppingList.remove('Banana')
print shoppingList
print

# loop through list
for item in shoppingList:
    print item

# length
print len(shoppingList)           # Anzahl der Elemente
print
