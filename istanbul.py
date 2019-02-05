import random, sys, os

print("\n\n\t --- Istanbul ---")
print("\n\n\t 1 Spielaufbau") 

while True:
        
    print("\n\t 2 Startspieler \n\n\t 3 Neues Spielfeld für VIPs \n\n\t 4 Exit ")



    # -- Spielfelder --

    istanbul = ["[-     Wagnerei     -]", "[-    Tuchlager     -]", "[-   Gewürzlager    -]", "[-    Obstlager     -]", "[-     Postamt      -]",  "[-   Karawanserei   -]",  "[-    Dönerbude     -]",  "[-   Schwarzmarkt   -]",  
                "[-     Teestube     -]", "[-  Kleiner Markt   -]", "[-   Großer Markt   -]", "[-   Polizeiwache   -]", "[-  Sultanspalast   -]", "[-  Kleine Moschee  -]", "[-  Große Moschee   -]","[- Edelsteinhändler -]","[-  Kaffeerösterei  -]", 
                "[-   Gildenhalle    -]", "[-     Taverne      -]", "[-    Kaffeehaus    -]"]

    user_input = input()

    # -- Exit -- 

    if user_input == "4":
        sys.exit()

    # -- Spielaufbau -- 

    elif user_input == "1":
        

        # -- Spielfeldausgabe Funktion -- 

        def print_istanbul():

            print("\n" * 3)
            print("\t",*istanbul[0:5])
            print("\n")
            print("\t",*istanbul[5:10])
            print("\n")
            print("\t",*istanbul[10:15])
            print("\n")
            print("\t",*istanbul[15:20])

            print("\n" * 3)

        # -- Spieldfeld - Shuffle

        random.shuffle(istanbul)


        # -- Dönerbude --

        db = istanbul.index("[-    Dönerbude     -]")
        inner_circle = ["6","7","8","11","12","13"]

        if  str(db) in inner_circle:

            pass
        else:

            while True:

                r = random.choice(istanbul)
                if str(istanbul.index(r)) in inner_circle:
                    istanbul[istanbul.index(r)], istanbul[db] = istanbul[db], istanbul[istanbul.index(r)]
                    break
                else:
                    continue
        
        # -- Schwarzmarkt / Teestube --

        sm = istanbul.index("[-   Schwarzmarkt   -]")
        ts = istanbul.index("[-     Teestube     -]")

        def schwarzstube(schw,teest=[]):

            if str(sm) == schw:
                if str(ts) in teest:
                    
                    while True:
                        
                        neu_ts = random.choice(istanbul)

                        if str(istanbul.index(neu_ts)) in teest:
                            continue
                        elif neu_ts == "[-    Dönerbude     -]":
                            continue

                        else:
                            break
                    
                    istanbul[istanbul.index(neu_ts)], istanbul[ts] = istanbul[ts], istanbul[istanbul.index(neu_ts)]

                else:
                    pass
            else:
                pass

        schwarzstube("0", ["0","1","2","3","4","5","6","10","15"]) 
        schwarzstube("1", ["0","1","2","3","4","5","6","7","11","16"]) 
        schwarzstube("2", ["0","1","2","3","4","8","6","7","12","17"]) 
        schwarzstube("3", ["0","1","2","3","4","7","8","9","13","18"]) 
        schwarzstube("4", ["0","1","2","3","4","8","9","14","19"]) 
        schwarzstube("5", ["0","1","5","6","7","8","9","10","11","15"]) 
        schwarzstube("6", ["0","1","2","5","6","7","8","9","10","11","12","16"]) 
        schwarzstube("7", ["1","2","3","5","6","7","8","9","11","12","13","17"]) 
        schwarzstube("8", ["1","2","3","5","6","7","8","9","12","13","14","18"]) 
        schwarzstube("9", ["3","4","5","6","7","8","9","13","14","19"]) 
        schwarzstube("10", ["0","5","6","10","11","12","13","14","15","16"]) 
        schwarzstube("11", ["1","5","6","7","10","11","12","13","14","15","16","17"]) 
        schwarzstube("12", ["2","6","7","8","10","11","12","13","14","16","17","18"]) 
        schwarzstube("13", ["3","7","8","9","10","11","12","13","14","17","18","19"]) 
        schwarzstube("14", ["4","8","9","10","11","12","13","14","18","19"]) 
        schwarzstube("15", ["0","5","10","11","15","16","17","18","19"])
        schwarzstube("16", ["1","6","10","11","12","15","16","17","18","19"])
        schwarzstube("17", ["2","7","11","12","13","15","16","17","18","19"])
        schwarzstube("18", ["3","8","12","13","14","15","16","17","18","19"])
        schwarzstube("19", ["4","9","13","14","15","16","17","18","19"])

        # -- Endausgabe Spielfeld --

        
        os.system("clear")
        print_istanbul()
        print("\n",("\t")*5,"-- Schmuggler auf       ", istanbul[random.randint(0,19)])                
        print("\n",("\t")*5,"-- Gouverneur auf       ", istanbul[random.randint(0,19)])                
        print("\n",("\t")*5,"-- Kaffehändler auf     ", istanbul[random.randint(0,19)],("\n" * 3))                



                
    # -- Gouverneur, Schmuggler, Kaffehändler --

    elif user_input == "3":

        print("\n\t-- Figur auf ", istanbul[random.randint(0,19)])
        print("\n" * 2)
        
    
    # -- Startspieler bestimmen

    elif user_input == "2":

        players = []
        
        anzahl_spieler = input("\nWieviele Spieler? ")
        count = 1

        while count <= int(anzahl_spieler):
            player = input("Wer ist der " + str(count) + ". Spieler?  ")
            players.append(player)
            count += 1

            if count > int(anzahl_spieler): 
                break
            else:
                continue
        os.system("clear")
        print("\n\n\t", random.choice(players) + " fängt an!\n\n")

             
    else: 
        print("\n\t-- Falsche Eingabe.")

        
