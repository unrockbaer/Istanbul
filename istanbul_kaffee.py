""" 

Programm zum Brettspiel Istanbul mit Erweiterung "Mokka und Bakschisch"

    Funktionen: 
        - erstellt einen zufälligen Spielplan für das Grundspiel mit der Erweiterung "Mokka und Bakschisch" gemäß Regeln
        - es wird berücksichtigt, dass sich die Dönerbude in der Mitte des Spielplans befindet
        - es wird berücksichtigt, dass die Teestube und Schwarzmarkt sich nicht auf der selben Linie befinden und mind. 3 Felder Abstand sind
        - Auswahl eines Startspielers
        - Auswahl eines zufälligen Feldes für Schmuggler, Kaffeehändler und Gouverneur

"""
def mokka():

        import random, sys, os

        os.system("clear")
        print("\n\n\t --- Istanbul ---")
        print("\n\n\t 1 Spielaufbau") 

        while True:
                
            print("\n\t 2 Startspieler \n\n\t 3 Neues Spielfeld für VIPs \n\n\t 4 Exit ")



        # -- SPIELFELDER --

            spielfelder = ["[-     Wagnerei     -]", "[-    Tuchlager     -]", "[-   Gewürzlager    -]", "[-    Obstlager     -]", "[-     Postamt      -]",  
                   "[-   Karawanserei   -]",  "[-    Dönerbude     -]",  "[-   Schwarzmarkt   -]", "[-     Teestube     -]", "[-  Kleiner Markt   -]", 
                   "[-   Großer Markt   -]", "[-   Polizeiwache   -]", "[-  Sultanspalast   -]", "[-  Kleine Moschee  -]", "[-  Große Moschee   -]",
                   "[- Edelsteinhändler -]","[-  Kaffeerösterei  -]", "[-   Gildenhalle    -]", "[-     Taverne      -]", "[-    Kaffeehaus    -]"]

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

                # -- Dönerbude darf sich nur in einem der inneren Felder befinden

                doenerbude = spielfelder.index("[-    Dönerbude     -]")
                innere_felder = ["6","7","8","11","12","13"]

                if  str(doenerbude) in innere_felder:

                    pass
                else:

                    while True:
                        
                        # -- Innenfeld wird ermittelt
                        r = random.choice(spielfelder)                      # r wird ein zufälliges Feld zugewiesen
                        if str(spielfelder.index(r)) in innere_felder:
                            spielfelder[spielfelder.index(r)], spielfelder[doenerbude] = spielfelder[doenerbude], spielfelder[spielfelder.index(r)]     # zufälliges Innenfeld mit Dönerbude getauscht
                            break
                        else:
                            continue
                
        # -- SCHARZMARKT / TEESTUBE --

                # -- Schwarzmarkt und Teestube dürfen sich nicht auf der selben Reihe oder Zeile befinden, außerdem mind. 3 Felder Abstand haben
                sm_index = spielfelder.index("[-   Schwarzmarkt   -]")
                ts_index = spielfelder.index("[-     Teestube     -]")

                # Dictionary für { Schwarzmarktfeld : (rote Zone) }
                roteZone = { 0 : ("0","1","2","3","4","5","6","10","15"),
                             1 : ("0","1","2","3","4","5","6","7","11","16"), 
                             2 : ("0","1","2","3","4","8","6","7","12","17"),
                             3 : ("0","1","2","3","4","7","8","9","13","18"),
                             4 : ("0","1","2","3","4","8","9","14","19"),
                             5 : ("0","1","5","6","7","8","9","10","11","15"),
                             6 : ("0","1","2","5","6","7","8","9","10","11","12","16"),
                             7 : ("1","2","3","5","6","7","8","9","11","12","13","17"),
                             8 : ("1","2","3","5","6","7","8","9","12","13","14","18"),
                             9 : ("3","4","5","6","7","8","9","13","14","19"),
                            10 : ("0","5","6","10","11","12","13","14","15","16"),
                            11 : ("1","5","6","7","10","11","12","13","14","15","16","17"),
                            12 : ("2","6","7","8","10","11","12","13","14","16","17","18"),
                            13 : ("3","7","8","9","10","11","12","13","14","17","18","19"),
                            14 : ("4","8","9","10","11","12","13","14","18","19"),
                            15 : ("0","5","10","11","15","16","17","18","19"),
                            16 : ("1","6","10","11","12","15","16","17","18","19"),
                            17 : ("2","7","11","12","13","15","16","17","18","19"),
                            18 : ("3","8","12","13","14","15","16","17","18","19"),
                            19 : ("4","9","13","14","15","16","17","18","19")
                            } 


                
                while True:
                    
                # - neu gewähltes Spielfeld, das nicht in der roten Zone ist, wird gesucht
                    tsNeuIndex = random.choice(spielfelder)

                # - wenn tsNeuIndex in der roten Zone liegt oder Dönerbude ist - continue
                    if str(spielfelder.index(tsNeuIndex)) in roteZone[sm_index]:
                        continue

                    elif tsNeuIndex == "[-    Dönerbude     -]":
                        continue

                    else:
                        break

                    # - gewähltes Spielfeld mit Teestube tauschen
                    spielfelder[spielfelder.index(tsNeuIndex)], spielfelder[ts_index] = spielfelder[ts_index], spielfelder[spielfelder.index(tsNeuIndex)]



        # -- ENDAUSGABE SPIELFELD --

                os.system("clear")
                print_spielfeld()
                print("\n",("\t")*5,"-- Schmuggler auf       ", spielfelder[random.randint(0,19)])                
                print("\n",("\t")*5,"-- Gouverneur auf       ", spielfelder[random.randint(0,19)])                
                print("\n",("\t")*5,"-- Kaffeehändler auf     ", spielfelder[random.randint(0,19)],("\n" * 3))                



                        
        # -- GOUVERNEUR, SCHMUGGLER, KAFFEHÄNDLER --

            elif user_input == "3":

                os.system("clear")
                print("\n\t-- Figur auf ", spielfelder[random.randint(0,19)])
                print("\n" * 2)
                
            
        # -- STARTSPIELER BESTIMMEN --

            elif user_input == "2":

                spielernamen = []
                
                anzahl_spieler = input("\nWieviele Spieler? ")
                print()

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

                
mokka()
