# -*- encoding: utf-8 -*-

secret = 33

guess = int(raw_input("Versuchen Sie doch Ihr Glück! Erraten Sie die Geheimzahl zwischen 1 und 100 und gewinnen Sie 5.000 Euro!\n"))


if guess == secret:
    print "Herzlichen Glückwunsch! Sie haben soeben gewonnen."

else:
    print "Leider ist das nicht die geheime Zahl."


