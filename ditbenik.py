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

question1 = input("Kies A, B of C: ")
if question1 == "A":
	print("Nee, ik deed de HAVO.")
elif question1 == "B":
	print("Klopt! Ik ben twee keer blijven zitten dus ik deed er 7 jaar over.")
else:
	print("Nee, ik deed de HAVO.")

print("\nWat doe ik voornamelijk in mijn vrije tijd?")

print("A. Gamen")
print("B. Met vrienden omgaan")
print("C. Niksen")

question2 = input("Kies A, B of C: ")
if question2 == "A":
	print("Klopt! Ik besteed het grootste deel van mijn vrije tijd aan gamen. Ik chat ook wel met vrienden maar ben meer met gamen bezig.")
elif question2 == "B":
	print("Soort van correct? Ik praat veel met vrienden online maar doe het meeste met gamen.")
else:
	print("Nope, ik game het meeste van mijn vrije tijd.")

print("\nWat doe ik als ik geen idee meer heb voor een vraag?\n")

print("A. Ik wacht tot ik een vraag verzin")
print("B. Ik vraag aan anderen of die een idee hebben")
print("C. Ik verzin zomaar een vraag die nergens op slaat")

question3 = input("Kies A, B of C: ")
if question3 == "C":
	print("Klopt! Hoe wist je dat? :^)")
else:
	print("Nope. :^) Hoe ben ik op deze vraag gekomen?")

print("\nBedankt voor het beantwoorden van deze vragen!")