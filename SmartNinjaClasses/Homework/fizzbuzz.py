# FIZZBUZZ

user_number = int(raw_input("Gib eine Zahl zwischen 1 und 100 ein und siehe was passiert: \n"))

i = 0

while i < 100:
    i += 1
    if i % 3 == 0:
        print "Fizz"
        continue
    elif i % 5 == 0:
        print "Buzz"
        continue
    elif i == user_number:
        break
    else:
        print i
print "Bei %s endet es!" % user_number