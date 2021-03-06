       
""" 

Programm zum Brettspiel Istanbul

	Funktionen: 
		- erstellt einen zufälligen Spielplan für das Grundspiel gemäß Regeln
		- es wird berücksichtigt, dass sich die Dönerbude in der Mitte des Spielplans befindet
		- es wird berücksichtigt, dass die Teestube und Schwarzmarkt mind. 3 Felder Abstand haben
		- Auswahl eines Startspielers
		- Auswahl eines zufälligen Feldes für Schmuggler und Gouverneur

"""
def grundspiel():

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
				   "[- Edelsteinhändler -]"]

			user_input = input()

		# -- EXIT -- 

			if user_input == "4":
				sys.exit()

		# -- SPIELAUFBAU -- 

			elif user_input == "1":
				

				# -- SPIELFELDAUSGABE FUNKTION -- 

				def print_spielfeld():

					print("\n" * 3)
					print("\t",*spielfelder[0:4])
					print("\n")
					print("\t",*spielfelder[4:8])
					print("\n")
					print("\t",*spielfelder[8:12])
					print("\n")
					print("\t",*spielfelder[12:16])

					print("\n" * 3)

				# -- Spieldfeld - Shuffle

				random.shuffle(spielfelder)


		# -- DÖNERBUDE --

				# -- Dönerbude darf sich nur in einem der inneren Felder befinden

				doenerbude = spielfelder.index("[-    Dönerbude     -]")
				innere_felder = ["5","6","9","10"]

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
				
		# -- ENDAUSGABE SPIELFELD --

				os.system("clear")
				print_spielfeld()
				print("\n",("\t")*3,"-- Schmuggler auf       ", spielfelder[random.randint(0,15)])                
				print("\n",("\t")*3,"-- Gouverneur auf       ", spielfelder[random.randint(0,15)],("\n" * 3))                



						
		# -- GOUVERNEUR, SCHMUGGLER, KAFFEHÄNDLER --

			elif user_input == "3":

				os.system("clear")
				print("\n\t-- Figur auf ", spielfelder[random.randint(0,15)])
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

grundspiel()
				
