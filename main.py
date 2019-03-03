import sys

print("\n\n\t --- Istanbul ---")
print("\n\n\t 1 Grundspiel")
print("\n\n\t 2 Erweiterung Mokka und Bakhschisch")
print("\n\n\t 3 Exit")

while True:
			
	user_in = input()

	if user_in == "1":
		from istanbul_grundspiel import grundspiel

	elif user_in == "2":
		from istanbul_kaffee import mokka

	elif user_in == "3":
		sys.exit()
	else:
		print("Falsche Eingabe")
