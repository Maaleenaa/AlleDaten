"""
dictionaries:
key-value-pairs
"""

myDict = {}
print myDict
print

# add element
myDict['name'] = 'Pater'           #auch def mit zb b={"Tier":"Adler","Alter":10}, name waere key , Pater value
# initialize with entry
newDict = {'phone': '066410100200'}
print newDict
print

# update with new
myDict.update(newDict)
print myDict
print

# view values:                           # gibt alle keys wieder
print myDict.keys()
print

# view values:                         # gibt alle values wieder
print myDict.values()
print

# view items                           # liste von tuples
print myDict.items()
print

# delete item                            # keys ansprechen umd einzelne zu loeschen
del myDict['phone']
print myDict
print

# clear entire dict
myDict.clear()
print myDict
print


# Taskmanager:
# key - value
# taskname : completed
myTasks={}
myTasks['Homework_Week9'] = {'taskname': 'Taskmanager', 'completed': False}

einkaufsliste = ['Banana', 'Milk']
# einkaufsliste[0] -> 'Banana'
# einkaufsliste[1] -> 'Milk'