""" 

Programm zum Brettspiel Istanbul

	Funktionen: 
		- erstellt einen zufälligen Spielplan für das Grundspiel mit der Erweiterung "Mokka und Bakschisch" gemäß Regeln
		- es wird berücksichtigt, dass sich das Teestubenfeld in der Mitte des Spielplans befindet
		- es wird berücksichtigt, dass die Teestube und Schwarzmarkt sich nicht auf der selben Linie befinden und mind. 3 Felder Abstand sind
		- Auswahl eines Startspielers
		- Auswahl eines zufälligen Feldes für Schmuggler, Kaffeehändler und Gouverneur

"""

import random, sys, os

print("\n\n\t --- Istanbul ---")
print("\n\n\t 1 Spielaufbau") 

while True:
        
    print("\n\t 2 Startspieler \n\n\t 3 Neues Spielfeld für VIPs \n\n\t 4 Exit ")



# -- SPIELFELDER --

    spielfelder = ["[-     Wagnerei     -]", "[-    Tuchlager     -]", "[-   Gewürzlager    -]", "[-    Obstlager     -]", "[-     Postamt      -]",  "[-   Karawanserei   -]",  "[-    Dönerbude     -]",  "[-   Schwarzmarkt   -]",  
                "[-     Teestube     -]", "[-  Kleiner Markt   -]", "[-   Großer Markt   -]", "[-   Polizeiwache   -]", "[-  Sultanspalast   -]", "[-  Kleine Moschee  -]", "[-  Große Moschee   -]","[- Edelsteinhändler -]","[-  Kaffeerösterei  -]", 
                "[-   Gildenhalle    -]", "[-     Taverne      -]", "[-    Kaffeehaus    -]"]

    user_input = input()

# -- EXIT -- 

    if user_input == "4":
        sys.exit()

# -- SPIELAUFBAU -- 

    elif user_input == "1":
        

        # -- SPIELFELDAUSGABE FUNKTION -- 

        def print_spielfeld():

            print("\n" * 3)
            print("\t",*spielfelder[0:5])
            print("\n")
            print("\t",*spielfelder[5:10])
            print("\n")
            print("\t",*spielfelder[10:15])
            print("\n")
            print("\t",*spielfelder[15:20])

            print("\n" * 3)

        # -- Spieldfeld - Shuffle

        random.shuffle(spielfelder)


# -- DÖNERBUDE --

        doenerbude = spielfelder.index("[-    Dönerbude     -]")
        innere_felder = ["6","7","8","11","12","13"]

        if  str(doenerbude) in innere_felder:

            pass
        else:

            while True:

                r = random.choice(spielfelder)
                if str(spielfelder.index(r)) in innere_felder:
                    spielfelder[spielfelder.index(r)], spielfelder[doenerbude] = spielfelder[doenerbude], spielfelder[spielfelder.index(r)]
                    break
                else:
                    continue
        
# -- SCHARZMARKT / TEESTUBE --

		# -- Schwarzmarkt und Teestube dürfen sich nicht auf der selben Reihe oder Zeile befinden, außerdem mind. 3 Felder Abstand haben
        sm_index = spielfelder.index("[-   Schwarzmarkt   -]")
        ts_index = spielfelder.index("[-     Teestube     -]")

        def schwarzmarkt_teestube(sm_feld,rote_zone=[]):   # - rote_zone sind Felder, auf der Teestube nicht sein darf

            if str(sm_index) == sm_feld:
                if str(ts_index) in rote_zone:
                    
                    while True:
                        
                    # - neu gewähltes Spielfeld, das nicht in der roten Zone ist, wird gesucht
                        tsNeuIndex = random.choice(spielfelder)

					# - wenn tsNeuIndex in der roten Zone liegt oder Dönerbude ist - continue
                        if str(spielfelder.index(tsNeuIndex)) in rote_zone:
                            continue
                        elif tsNeuIndex == "[-    Dönerbude     -]":
                            continue

                        else:
                            break

					# - gewähltes Spielfeld mit Teestube tauschen
                    spielfelder[spielfelder.index(tsNeuIndex)], spielfelder[ts_index] = spielfelder[ts_index], spielfelder[spielfelder.index(tsNeuIndex)]

                else:
                    pass
            else:
                pass

		# Prüfung für jedes Feld, ob Index von Schwarzmarkt und wenn ja, ob Teestube in roter_zone

        schwarzmarkt_teestube("0", ["0","1","2","3","4","5","6","10","15"]) 
        schwarzmarkt_teestube("1", ["0","1","2","3","4","5","6","7","11","16"]) 
        schwarzmarkt_teestube("2", ["0","1","2","3","4","8","6","7","12","17"]) 
        schwarzmarkt_teestube("3", ["0","1","2","3","4","7","8","9","13","18"]) 
        schwarzmarkt_teestube("4", ["0","1","2","3","4","8","9","14","19"]) 
        schwarzmarkt_teestube("5", ["0","1","5","6","7","8","9","10","11","15"]) 
        schwarzmarkt_teestube("6", ["0","1","2","5","6","7","8","9","10","11","12","16"]) 
        schwarzmarkt_teestube("7", ["1","2","3","5","6","7","8","9","11","12","13","17"]) 
        schwarzmarkt_teestube("8", ["1","2","3","5","6","7","8","9","12","13","14","18"]) 
        schwarzmarkt_teestube("9", ["3","4","5","6","7","8","9","13","14","19"]) 
        schwarzmarkt_teestube("10", ["0","5","6","10","11","12","13","14","15","16"]) 
        schwarzmarkt_teestube("11", ["1","5","6","7","10","11","12","13","14","15","16","17"]) 
        schwarzmarkt_teestube("12", ["2","6","7","8","10","11","12","13","14","16","17","18"]) 
        schwarzmarkt_teestube("13", ["3","7","8","9","10","11","12","13","14","17","18","19"]) 
        schwarzmarkt_teestube("14", ["4","8","9","10","11","12","13","14","18","19"]) 
        schwarzmarkt_teestube("15", ["0","5","10","11","15","16","17","18","19"])
        schwarzmarkt_teestube("16", ["1","6","10","11","12","15","16","17","18","19"])
        schwarzmarkt_teestube("17", ["2","7","11","12","13","15","16","17","18","19"])
        schwarzmarkt_teestube("18", ["3","8","12","13","14","15","16","17","18","19"])
        schwarzmarkt_teestube("19", ["4","9","13","14","15","16","17","18","19"])

# -- ENDAUSGABE SPIELFELD --

        os.system("clear")
        print_spielfeld()
        print("\n",("\t")*5,"-- Schmuggler auf       ", spielfelder[random.randint(0,19)])                
        print("\n",("\t")*5,"-- Gouverneur auf       ", spielfelder[random.randint(0,19)])                
        print("\n",("\t")*5,"-- Kaffehändler auf     ", spielfelder[random.randint(0,19)],("\n" * 3))                



                
# -- GOUVERNEUR, SCHMUGGLER, KAFFEHÄNDLER --

    elif user_input == "3":

        os.system("clear")
        print("\n\t-- Figur auf ", spielfelder[random.randint(0,19)])
        print("\n" * 2)
        
    
# -- STARTSPIELER BESTIMMEN --

    elif user_input == "2":

        spielernamen = []
        
        anzahl_spieler = input("\nWieviele Spieler? ")
        count = 1

        while count <= int(anzahl_spieler):
            name = input("Wer ist der " + str(count) + ". Spieler?  ")
            spielernamen.append(name)
            count += 1

            if count > int(anzahl_spieler): 
                break
            else:
                continue
        os.system("clear")
        print("\n\n\t", random.choice(spielernamen) + " fängt an!\n\n")

             
    else: 
        print("\n\t-- Falsche Eingabe.")

        
