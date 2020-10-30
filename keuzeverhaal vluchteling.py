import time
import os

def beginVerhaal():
    print("""
                        Begin van het verhaal.
            
            Dit is het verhaal van de Syrische fotograaf Mohammad Abdulazez, komende uit Homs.
            Hij woonde tijdens een burgeroorlog in Homs. Uiteindelijk werd het hem te heet onder de voeten en besloot hij naar de Turkse grensplaats Gaziantep te vluchten.
            Zijn familie volgden hem niet veel later. Later is hij opnieuw gevlucht naar Nederland. Maak jij hetzelfde verhaal als hem mee of lukt het jou niet om de reis te voltooien?""")
    deel1()

def deel1():
    print("""
                        Deel 1: Oorlog in Homs 
            
            Er is een burgeroorlog uitgebroken in Homs. Homs wordt gezien als een bolwerk voor het verzet tegen president Bashar al-Assad.
            Homs is het symbool van de revolutie. Het leger van de regering heeft de stad omringd en er vallen iedere dag meer en meer doden.
            Nu rust bij jou de keuze.
            
            Blijf je schuilen of ga je hulp zoeken? 
          """)
    answer = input("A. Schuilen \nB. Hulp Zoeken\n")
    if answer == "A" or answer == "a":
        os.system('cls')
        deel3()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel2()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        beginVerhaal()

def deel2():
    print("""
                        Deel 2: Hulp zoeken 
            
            Je besluit om hulp te zoeken in Homs. De stad is omringd dus hulp van buiten vragen gaat niet lukken.
            Je blijft zoeken en vindt uiteindelijk een groep mensen. Je wordt benaderd door de groep en he zijn leden van het verzet.
            Ze vragen of je mee wilt werken aan de revolutie.
            
            Wat wordt het?
          """)
    answer = input("A. Je doet mee aan de revolutie \nB. Je besluit om te blijven zoeken\n")
    if answer == "A" or answer == "a":
        os.system('cls')
        eind1()
    elif answer == "B" or answer == "b":
        os.system('cls')
        deel4()
    else:
        print("Kies A of B!")
        time.sleep(2)
        os.system('cls')
        deel2()

def deel3():
	print("""
                        Deel 3: Schuilen
            
            Je besluit je beschut te houden op een veilige locatie. Je wacht iedere dag in angst tot er iemand komt om te helpen. Uiteindelijk komt het.
            De regering laat mensen uit Homs vluchten vanwege de leefomstandigheden van de gemiddelde bewoner.
            Langzaam halen ze de stad leeg en jij, samen met je familie worden veilig uit Homs gehaald.
            
            Maar wat nu? Waar ga je nu naartoe?
		  """)
	answer = input("A. Blijf in Syrië en zoek een nieuwe woonplaats \nB. Vlucht richting het noorden, uit Syrië \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel5()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel6()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel3()

def deel4():
	print("""
                        Deel 4: Verder zoeken
    
            Je besluit niet aan de revolutie mee te doen en in plaats daarvan verder te zoeken. Je kan uiteindelijk geen hulp vinden maar hebt wel een ander idee.
            
            Ga je voor levensmiddelen zoeken of ga je toch weer schuilen? 
		  """)
	answer = input("A. Levensmiddelen zoeken \nB. Opnieuw schuilen \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		eind2()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel3()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel4()

def deel5():
	print("""
                        Deel 5: Een nieuw thuis
            
            Je besluit om binnen Syrië te blijven en een nieuw thuis te vinden. Na een lange zoektocht heb je een nieuwe, voorlopig veilige woonplaats gevonden.
            Iets later lichtte jij je familie in en zij zijn niet veel later ook gevlucht. Je leeft nog steeds iedere dag in angst dat de burgeroorlog zich tot jouw stad verspreidt maar dat gevoel wordt elke dag minder.
            Toch ben je niet gelukkig in je nieuwe huis.
            
            Denk je eraan om verder te vluchten of blijf je bij je familie? 
		  """)
	answer = input("A. Verder vluchten \nB. Bij je familie blijven \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel6()
	elif answer == "B" or answer == "b":
		os.system('cls')
		eind3()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel5()

def deel6():
	print("""
                        Deel 6: Eind van de vlucht? 

            Je besluit om verder te vluchten, richting het noorden. De reis is lang maar je zet door, je wilt blijdschap vinden.
            Je komt uiteindelijk aan in Turkije, in Gaziantep. Opnieuw licht je je familie in en ze zijn erg blij dat je een goede, rustige plek hebt gevonden in Turkije.
            Iedereen is blij en iedereen heeft een baan gevonden.  Eind goed al goed. 

            Of toch niet? Na twee jaar ben je ongelukkig.
            Je werkte als fixer voor internationale media waarvoor je soms terug moest naar Syrië, maar de media heeft zijn belangstelling in het conflict verloren.
            Je hebt geen baan meer. Je verveelt je. Al je vrienden zijn al naar Europa vertrokken en wachten om terug te gaan heeft geen zin. De oorlog in Syrië zal nog jaren duren.
            Je besluit naar het noorden te vertrekken. Je ouders zijn verdrietig maar ze snappen het volkomen.
            
            Je wilt verder met je leven. 
		  """)
	answer = input("A. Ga verder met het verhaal \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel7()
	else:
		print("Kies A om verder te gaan.")
		time.sleep(2)
		os.system('cls')
		deel6()

def deel7():
	print("""
                        Deel 7: Istanbul 

            Je had besloten om met het vliegtuig richting Istanbul te gaan. Daar heb je de groep, die bestaat uit 25 anderen, ontmoet.
            Allemaal willen jullie naar Europa. Jullie hebben een goede voorbereiding gemaakt. Omdat het zo’n grote groep is, is er ook een groot netwerk ontstaan.
            Mensen zijn op de hoogte gebracht van jullie komst en dat zorgt voor veel rust. Maar een goede voorbereiding geeft geen garantie voor een geslaagde reis.
            Het weer is verschrikkelijk maar toch moet de reis gemaakt worden. De volgende stad is Izmir, en van daar wordt het een bootreis.
            
            Hoe ga je verder? 
		  """)
	answer = input("A. Blijf bij de groep \nB. Ga alleen verder en ontmoet de groep later weer \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel9()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel8()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel7()

def deel8():
	print("""
                        Deel 8: Alleen reizen 

            Je plan was om alleen verder te reizen tot Izmir. De trip duurde langer dan het eigenlijk was.
            Je was de hele tijd alleen en je had niet veel spullen meegenomen, dus veel was er ook niet te doen.
            Onderweg kwam je een groep mensen tegen die zo aardig waren om een aanbod te doen om jou naar je bestemming te brengen.
            
            Ga je met ze mee of reis je alleen verder? 
		  """)
	answer = input("A. Reis met ze mee \nB. Maak de reis verder alleen af \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel9()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel10()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel8()

def deel9():
	print("""
                        Deel 9: Izmir 

            Je bent samen naar Izmir gegaan. Daar hebben jullie een smokkelaar gevonden die jullie vertrouwden.
            Het was duur om iedereen een plek te garanderen, maar dat hadden jullie ervoor over. Vanaf dat punt werd het wachten op de boot richting Griekenland.
            Het wachten duurde niet lang en uiteindelijk kwam iedereen bij elkaar op de verschillende boten. Er is nog een lange reis te gaan maar gelukkig ben je niet meer alleen.
            Hoewel er meer vluchtelingen waren dan afgesproken met de smokkelaars, ziet het er goed uit. 
		  """)
	answer = input("A. Wacht tot de reis over is \nB. Maak contact met andere mensen in de groep \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel11()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel12()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel9()

def deel10():
	print("""
                        Deel 10: Alleen verder 

            Uiteindelijk ben je aangekomen in Izmir en daar de andere groep weer ontmoet.
            Ze vroegen zich wel af waar je was maar na een gesprek heb je verteld dat je liever alleen reisde.
            De groep had al een smokkelaar gevonden die zij vertrouwden en hebben voor jou ook een plek geregeld, je hoefde alleen nog maar te betalen.
            Na dat afgehandeld te hebben zijn jullie uiteindelijk allemaal naar de boten gebracht en op reis gezet naar Griekenland. 
		  """)
	answer = input("A. Wacht tot de reis over is \nB. Maak contact met andere mensen in de groep \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel11()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel12()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel10()

def deel11():
	print("""
                        Deel 11 

            Je besluit om jezelf af te sluiten van de rest van de groep en gewoon te wachten tot je aankomt op de eindbestemming.
            De rest van de mensen op jouw boot zaten wel gezellig te praten maar je zat je meer zorgen te maken over de rest van de reis. Toen jullie Lesbos bijna bereikten, sloeg het weer om.
            De golven werden hoger en het water sloeg de boot in. Jullie hadden allemaal de keus gemaakt om al de bagage overboord te gooien om de boot lichter te maken.
            Met jullie jassen hebben jullie het water uit de boot gehaald en zo veilig de rest van de bootreis afgemaakt. Toen jullie in Mytilini aankwamen waren jullie verplicht om jullie te laten registreren.
            Bij de een duurde dat langer dan de ander. Daarom heb jij samen met vier anderen besloten om van de grote groep te splitsen.
            Zo konden jullie sneller verder met de vlucht, waarvoor jullie kaartjes nodig hadden voor de Ferry naar Athene.
            Uiteindelijk aangekomen in Athene kon je de trein nemen of iemand vinden om jou naar Kroatië te brengen via de boot.
            
            Welke neem jij? 
		  """)
	answer = input("A. De trein \nB. De boot \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel14()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel13()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel11()

def deel12():
	print("""
                        Deel 12 

            Je dacht dat het wel een goed idee was om met mensen kennis te maken.
            Je was erachter gekomen dat je groep voornamelijk uit hoogopgeleide jongeren bestaat. De meeste werkten als media-activist, voor een ngo, mensenrechtenorganisatie of als fotograaf.
            Via hun zijn kennissen, vrijwilligers en ngo’s ingelicht over jullie komst. Op die manier hebben jullie het nummer van de kustwacht bemachtigd mochten jullie in de problemen raken. 

            Jammer genoeg gebeurde dat ook. Toen jullie Lesbos bijna bereikten, sloeg het weer om. De golven werden hoger en het water sloeg de boot in.
            Jullie hadden allemaal de keus gemaakt om al de bagage overboord te gooien om de boot lichter te maken. Met jullie jassen hebben jullie het water uit de boot gehaald en zo veilig de rest van de bootreis afgemaakt.
            Toen jullie in Mytilini aankwamen waren jullie verplicht om jullie te laten registreren. Bij de een duurde dat langer dan de ander.
            Daarom heb jij samen met vier anderen besloten om van de grote groep te splitsen, zo konden jullie sneller verder met de vlucht, waarvoor jullie kaartjes nodig hadden voor de Ferry naar Athene.
            Uiteindelijk aangekomen in Athene kon je de trein nemen of iemand vinden om jou naar Kroatië te brengen via de boot.
            
            Welke neem jij? 
		  """)
	answer = input("A. De boot \nB. De trein \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel14()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel13()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel12()

def deel13():
	print("""
                        Deel 13: Verder met de vlucht 

            Jullie namen de trein en arriveerden ‘s nachts in Macedonië. Het regende. In het grensgebied krioelde het van de vluchtelingen.
            Iedereen werd doorgesluisd naar een speciale vluchtelingentrein die jullie naar het Servische grensgebied zou brengen.
            Aan de grens moesten jullie je weer laten registreren, wat nog langer duurde dan de vorige keer. Uiteindelijk zijn jullie drie dagen in het huis aan de grens gebleven.
            Jullie konden niet anders dan wachten. Na het registreren hadden jullie gelijk de bus naar Belgrado gepakt.
            Jullie hadden een heel goed hostel gevonden in het centrum, waar kleren gewassen konden worden en jullie een douche konden nemen.
            
            Hoe gaan jullie verder? 
		  """)
	answer = input("A. Via de trein \nB. Andere hulp zoeken \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel16()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel15()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel13()

def deel14():
	print("""
                        Deel 14: Nieuwe bootreis 

            Je had besloten om makkelijk langs de grenzen te komen en een bootreis te nemen.
            Je probeerde iemand te vinden die vertrouwelijk over kwam. Uiteindelijk heb je iemand betaald om jou mee te nemen naar Kroatië en jou daar af te zetten.
            Samen met een paar andere vluchtelingen zijn jullie de boot ingestapt en afwachtend stil gezeten. Onderweg werden jullie gestopt door de politie om te kijken wat er aan de hand was.
            In paniek zaten jullie te denken wat te doen.
            
            Blijf je zitten of ga je je verstoppen op de boot? 
		  """)
	answer = input("A. Blijf zitten waar je zit \nB. Verstoppen \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		eind4()
	elif answer == "B" or answer == "b":
		os.system('cls')
		deel17()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		deel14()

def deel15():
	print("""
                        Deel 15: Hulp uit een andere hoek 

            Een beetje zat van alle treinreizen en bootreizen hebben jullie besloten om wat persoonlijkere hulp te zoeken.
            Na een poos zoeken hebben jullie iemand gevonden die jullie naar de grens wouden brengen. Daar hebben jullie geen nee tegen gezegd en zijn netjes bij de grens uitgestapt.
            Er was geen andere optie dan lopend de grens over naar Hongarije. Jullie besloten in Hongarije maar een trein naar Oostenrijk te nemen en daar het beste van te nemen. 

            De treinreis duurde uiteindelijk 16 uur, hoewel de rit aanvankelijk vijf uur zou duren.
            Iedereen kreeg een flesje water van een halve liter en daar moesten jullie het mee doen.
            Er was in de trein verder geen eten of drinken. Jullie probeerden te slapen maar dat zou niet lukken.
            Er waren geen zitplaatsen over dus jullie konden alleen staan.
            
            Uiteindelijk waren jullie in Oostenrijk aangekomen. 
		  """)
	answer = input("A. Verder met het verhaal\n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel18()
	else:
		print("Kies A om verder te gaan.")
		time.sleep(2)
		os.system('cls')
		deel15()

def deel16():
	print("""
                        Deel 16: Een helse treinreis 

            De beslissing was snel gemaakt, weer met de trein.
            In Kroatië aangekomen pakten jullie een bus naar Hongarije.
            Jullie werden uitgebreid gefouilleerd voordat jullie de bus in konden.
            In Hongarije aangekomen stapten jullie over op een trein richting Oostenrijk. 

            De treinreis duurde uiteindelijk 16 uur, hoewel de rit aanvankelijk vijf uur zou duren.
            Iedereen kreeg een flesje water van een halve liter en daar moesten jullie het mee doen.
            Er was in de trein verder geen eten of drinken. Jullie probeerden te slapen maar dat zou niet lukken.
            Er waren geen zitplaatsen over dus jullie konden alleen staan.
            
            Uiteindelijk waren jullie in Oostenrijk aangekomen. 
		  """)
	answer = input("A. Ga verder met het verhaal \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel18()
	else:
		print("Kies A om verder te gaan")
		time.sleep(2)
		os.system('cls')
		deel16()

def deel17():
	print("""
                        Deel 17: Einde van de bootreizen 

            Je besloot om je te verstoppen. Dat bleek goed uit te pakken want na korte tijd ging de boot weer verder.
            Jullie zijn onopgemerkt in een rustige haven uitgestapt. Zo snel mogelijk zijn jullie richting Zagreb gegaan en van daar een bus naar Hongarije gepakt.
            In Hongarije aangekomen wouden jullie snel verder. Iets aan het land zat jullie niet zo lekker en hebben jullie dus snel een treinroute gezocht naar Oostenrijk. 

            De treinreis duurde uiteindelijk 16 uur, hoewel de rit aanvankelijk vijf uur zou duren.
            Iedereen kreeg een flesje water van een halve liter en daar moesten jullie het mee doen.
            Er was in de trein verder geen eten of drinken. Jullie probeerden te slapen maar dat zou niet lukken.
            Er waren geen zitplaatsen over dus jullie konden alleen staan.
            
            Uiteindelijk waren jullie in Oostenrijk aangekomen. 
		  """)
	answer = input("A. Ga verder met het verhaal \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel18()
	else:
		print("Kies A om verder te gaan.")
		time.sleep(2)
		os.system('cls')
		deel17()

def deel18():
	print("""
                        Deel 18: Een laatste drempel 

            Na die vreselijke reis in de Hongaarse trein werden jullie met open armen ontvangen in Oostenrijk.
            Vrijwilligers stonden klaar met eten, drinken en medicijnen. Er waren ook bussen om vluchtelingen naar Wenen te brengen.
            Om tijd te besparen hadden jullie een taxi naar Wenen gepakt. ‘s Avonds kwamen jullie in Wenen aan.
            Een paar dagen later hebben jullie via een online meeliftdienst geregeld dat jullie kunnen meeliften naar Salzburg.
            Daar aangekomen kwamen jullie erachter dat er geen vluchtelingentreinen naar Duitsland reden. Gelukkig kwamen jullie iemand tegen die een idee had.
            Jullie konden op een toeristenboot meevaren die langs Donau voer. 
		  """)
	answer = input("A. Verder met het verhaal \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		eind5()
	else:
		print("Kies A om verder te gaan")
		time.sleep(2)
		os.system('cls')
		deel18()

def eind1():
	print("""
                        Eind 1: De Revolutie 

            Je sluit je aan bij de revolutie, niet wetende wat er allemaal precies gebeurt.
            Het duurt niet lang voordat je een vuurwapen in je handen krijgt en je dagelijks tegen de regering moet vechten.
            Uiteindelijk wordt je onopgemerkt bewusteloos gemaakt en enkele uren later kom je weer bij.
            
            Je bevindt je in de gevangenis en je wordt ondervraagd, maar je weet van niets.
            Hier zit je de rest van je leven en is je verhaal voorbij. 
		  """)
	answer = input("A. Terug naar vorige keuze \nB. Stoppen met het verhaal \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel2()
	elif answer == "B" or answer == "b":
		print("Bedankt voor het spelen!")
		time.sleep(2)
		os.system('cls')
		exit()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		eind1()

def eind2():
	print("""
                        Eind 2: Levensmiddelen 

            Je besluit naar levensmiddelen te zoeken in de verlaten gebouwen van de stad.
            Zonder het te merken zit je midden in de vuurlinie tussen de rebellen en de regering.
            Je wordt geraakt door een van de explosies en komt zo aan je einde. 
		  """)
	answer = input("A. Terug naar vorige keuze \nB. Stoppen met het verhaal \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel4()
	elif answer == "B" or answer == "b":
		print("Bedankt voor het spelen!")
		time.sleep(2)
		os.system('cls')
		exit()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		eind2()

def eind3():
	print("""
                        Eind 3: Niet gevlucht 

            Toch vind je het wel best om bij je familie te blijven.
            Iedereen is voorlopig veilig en weer bij elkaar. Zolang dat zo is, is iedereen blij, toch?
            Ver weg van Homs en je bevindt je niet meer in de burgeroorlog.
            
            Toch blijf je die angst wel voelen, en terecht.
            Je bent niet uit Syrië gevlucht dus wie weet wat er later altijd nog kan gebeuren. 
		  """)
	answer = input("A. Terug naar vorige keuze \nB. Stoppen met het verhaal \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel5()
	elif answer == "B" or answer == "b":
		print("Bedankt voor het spelen!")
		time.sleep(2)
		os.system('cls')
		exit()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		eind3()

def eind4():
	print("""
                        Eind 4: Illegaal de grens over! 

            Toen je bleef zitten kwam de politie na een schip onderzoek achter jouw locatie.
            Zonder registratie de grens over proberen te komen is illegaal.
            Je was opgepakt en voor onbepaalde tijd achter de tralies gezet. 
		  """)
	answer = input("A. Terug naar vorige keuze \nB. Stoppen met het verhaal \n")
	if answer == "A" or answer == "a":
		os.system('cls')
		deel14()
	elif answer == "B" or answer == "b":
		print("Bedankt voor het spelen!")
		time.sleep(2)
		os.system('cls')
		exit()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		eind4()

def eind5():
	print("""
                        Eind 5: Een vlekkeloos ritje 

            Na zes uur kwamen jullie zonder problemen aan in Passau, Duitsland.
            Vanuit Passau hebben jullie de bus naar Bonn gepakt. De eindbestemming van een van de jongens uit de groep.
            Ook twee anderen willen in Duitsland blijven, en de laatste wilt naar Zweden.
            
            Zelf heb je inmiddels besloten om naar Nederland te gaan. Daar woont een neef van je.
            Je hebt de trein gepakt naar Amsterdam en daar iemand ontmoet die informatie verstrekte aan vluchtelingen.
            Hij vertelde veel over de procedure van nieuwkomers in Nederland. 
            Uiteindelijk heb je jezelf in Ter Apel laten registreren en heb je in Nijmegen een tentenkamp gevonden.
            Je zal hier voorlopig vier maanden moeten blijven, maar je voelt je weer veilig en vertrouwd.
            
            Je begint je nieuwe leven met vreugde. 
		  """)
	trueEnd = input("Gefeliciteerd! Je hebt het beste einde gekregen! Wil je opnieuw spelen om de andere eindes te vinden? \nA. Opnieuw \nB. Stoppen met spelen \n")
	if trueEnd == "A" or trueEnd == "a":
		os.system('cls')
		beginVerhaal()
	elif trueEnd == "B" or trueEnd == "b":
		print("Bedankt voor het spelen!")
		time.sleep(2)
		os.system('cls')
		exit()
	else:
		print("Kies A of B!")
		time.sleep(2)
		os.system('cls')
		eind5()
    

os.system('cls')
beginVerhaal()
