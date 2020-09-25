print("Hello You!, ik ben Martijn.")
print("Wie ben jij?")
naam = input()
print("Hello",naam)

print("\nIk ben een nieuwkomer op het Mediacollege Amsterdam.")
print("Door een aantal vragen over mij te beantwoorden leer je mij beter kennen!")

print("\nTijdens mijn middelbare school periode heb ik op dit niveau gezeten:")

print("A. VWO")
print("B. HAVO")
print("C. VMBO")

question = input("Kies A, B of C: ")
if question == "A":
	print("Nee, ik deed de HAVO.")
elif question == "B":
	print("Klopt! Ik ben twee keer blijven zitten dus ik deed er 7 jaar over.")
else:
	print("Nee, ik deed de HAVO.")

print("\nWat doe ik voornamelijk in mijn vrije tijd?")

print("A. Gamen")
print("B. Met vrienden omgaan")
print("C. Niksen")

question = input("Kies A, B of C: ")
if question == "A":
	print("Klopt! Ik besteed het grootste deel van mijn vrije tijd aan gamen. Ik chat ook wel met vrienden maar ben meer met gamen bezig.")
elif question == "B":
	print("Soort van correct? Ik praat veel met vrienden online maar doe het meeste met gamen.")
else:
	print("Nope, ik game het meeste van mijn vrije tijd.")

print("\nWelk muziek-instrument bespeelde ik?")

print("A. Gitaar")
print("B. Drums")
print("C. Keyboard")

question = input("Kies A, B of C: ")
if question == "C":
	print("Klopt! Hoe wist je dat?")
else:
	print("Nope. Het goede antwoord was Keyboard!")

print("\nWaar wil je meer over te weten komen:")

print("A. Gamen")
print("B. Hardlopen")
print("C. Muziek")

question = input("Kies A, B of C: ")
if question == "A":
	print("Oke! Hier nog een vraag:")

	print("\nWat voor games wil ik later maken?")

	print("A. First Person Shooter")
	print("B. 3D Platformer")
	print("C. Puzzle")

	question = input("Kies A, B of C: ")
	if question == "B":
		print("Klopt! 3D Platformers heb ik altijd van gehouden en houden altijd al een speciaal plekje bij mij.")
	else:
		print("Nee, sorry. 3D Platformers heb ik altijd van gehouden. Dat wil ik het liefst doen.")

	print("Bedankt voor het beantwoorden van deze vragen! Leuk dat je meer wou weten over mijn game-geschiedenis.")
elif question == "B":
	print("Oke! Hier nog een vraag:")

	print("\nHoe lang doe ik al aan hardlopen?")

	print("A. 4 jaar")
	print("B. 6 jaar")
	print("C. 8 jaar")

	question = input("Kies A, B of C: ")
	if question == "A":
		print("Klopt! Ik doe het al een tijdje en loop voornamelijk samen met vrienden.")
	else:
		print("Nee, fout! Ik doe al ongeveer 4 jaar aan hardlopen.")

	print("Bedankt voor het beantwoorden van deze vragen! Leuk dat je nog meer wou weten over sport.")
else:
	print("Oke! Hier nog een vraag:")

	print("\nVan wat voor muziek hou ik?")

	print("A. Metal")
	print("B. Klassiek")
	print("C. Van alles wat")

	question = input("Kies A, B of C: ")
	if question == "C":
		print("Dat is correct! Ik luister zo'n beetje naar alles, zolang het maar niet iets zoals Rap of Hardcore is.")
	else:
		print("Ja, op zich wel. Ik luister zo'n beetje naar alles.")
	
	print("Bedankt voor het beantwoorden van deze vragen! Leuk dat je nog meer wou weten over muziek.")