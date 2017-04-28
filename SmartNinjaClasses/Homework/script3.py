# coding=utf-8
"""
script3.py: Usereingabe Beispiele, Zahlen
"""

if __name__ == '__main__':

    # Eingabe Zahl
    try:

        zahl = raw_input("Nenne eine Zahl bitte")

        zahl = float(zahl)

        # Berechnung der Haelfte
        msg = zahl / 2.

        # Ausgabe der Haelftez
        print msg

    except:
        print "Sorry, your entry could not be interpreted"
        print "Please enter a valid number next time"
