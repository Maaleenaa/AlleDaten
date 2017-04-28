# coding=utf-8
"""
script3.py: Usereingabe Beispiele, Zahlen
"""

import random
secret = random.randint(1,10)

if __name__ == '__main__':

    # Eingabe Zahl
    while True:
        try:
            zahl = raw_input("Ich wette du errätst die geheime Zahl nie!\n")

            zahl = float(zahl)

            if zahl == secret:
                    print "Glückwunsch!"
                    break
            elif zahl > secret:
                    print "Leider Nein!"

            else:
                    print "Leider falsch, versuch es noch einmal!"

        except:
            print "Sorry, your entry could not be interpreted"
            print "Please enter a valid number next time"
