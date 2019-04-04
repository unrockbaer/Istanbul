#! /usr/bin/python3.7

""" Istanbul Brettspiel Begleitprogramm """

""" Dieses Programm erstellt einen Spielaufbau für Istanbul und erwürfelt neue Spielfelder. """

import sys, os

os.system("clear")

print("\n\n\t --- Istanbul ---")
print("\n\n\t 1 Grundspiel")
print("\n\n\t 2 Erweiterung Mokka und Bakschisch")
print("\n\n\t 3 Erweiterung Brief und Siegel")
print("\n\n\t 4 Der Große Basar")
print("\n\n\t 5 Exit")

while True:
			
	user_in = input()

	if user_in == "1":
		from istanbul_grundspiel import grundspiel

	elif user_in == "2":
		from istanbul_kaffee import mokka

	elif user_in == "3":
		from istanbul_briefUndSiegel import briefUndSiegel

	elif user_in == "4":
		from istanbul_basar import basar

	elif user_in == "5":
		sys.exit()
	else:
		print("Falsche Eingabe")
