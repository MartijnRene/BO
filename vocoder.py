from microbit import *
import speech
import random

lengtewoordarray = 3

onderwerp = ["she", "Ed", "Rosmerta"]
werkwoord = ["walks",  "learns", "drinks"]
rest = ["hard", "at school", "coffee"]

def sayTheWords1(word):
	print(word)
	speech.say(word, speed=120, pitch=100, throat=100, mouth=200)
	sleep(500)
	
def sayTheWords2():
	willekeurigGetal = random.randint(0, lengtewoordarray-1)
	display.show(willekeurigGetal)
	sayTheWords1(onderwerp[willekeurigGetal])
	sayTheWords1(werkwoord[willekeurigGetal])
	sayTheWords1(rest[willekeurigGetal])
	
while True:
	if button_a.is_pressed():
		display.show(Image.HAPPY)
		sayTheWords1("dat maakt mij blij")
	elif button_b.is_pressed():
		display.show(Image.SAD)
		sayTheWords1("dat doet pijn")
	elif display.read_light_level() <40:
		sayTheWords2()
	else:
	    display.show(Image.SQUARE)