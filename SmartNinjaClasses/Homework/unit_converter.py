#unit converter

# Begruessung
print "Hello User! I am here too help you convert kilometers into miles!"

# Kilometereingabe vom User
kilometers = raw_input("Enter value in kilometers: \n")
kilometers = float(kilometers)

# Umwandlungsfaktor
con_value = 0.621371

# Rechner
miles = kilometers * con_value
print ("%s kilometers is equal to %s miles" % (kilometers, miles))

while True:

 # Will der User noch einen Wert umrechnen?
    question2 = raw_input("Do you want to enter another value (Y/N)??")

    if question2 == "Y":
        print "Start the program again cause I dont know how to skip to the beginning."
        # Kilometereingabe vom User
        kilometers = raw_input("Enter value in kilometers: \n")

        # Umwandlungsfaktor
        con_value = 0.621371

        # Rechner
        miles = kilometers * con_value
        print ("%s kilometers is equal to %s miles" % (kilometers, miles))

    elif question2 == "N":
        print "Thank you and see you next time!"
        break
    else:
        print "That is not what you should type in, try again"
