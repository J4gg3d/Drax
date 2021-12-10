import random as rng
import time

print("How is invisible?")
print("1. Drax")
print("0. ???")

isrun = 0


def Drax(isrun):
	optionen = ["Taste 1a", "Taste 2a", "Taste 3a"]
	zeit = [1, 2, 5, 15, 20, 30]
	
	if isrun == 2:
		print("Drax TEST-movement:")
		try:
			while isrun == 2:
				print("*" * 30)
				print(rng.choice(optionen))
				pause = rng.choice(zeit)
				print(f"Wartezeit: {pause}")
				time.sleep(pause)
		except KeyboardInterrupt:
			print("Drax: DAMN!")
			pass
	elif isrun == 1:
		print("Drax incredible movment")
		try:
			while isrun == 1:
				pause = rng.choice(zeit)
				print(f"Wartezeit: {pause}")
				bewegung = rng.choice(optionen)
				if bewegung == "Taste 1a":
					print("*" * 30)
					print("Taste 1a")
					#keyboardbefehl hinzufügen
				elif bewegung == "Taste 2a":
					print("*" * 30)
					print("Taste 2a")
					#keyboardbefehl hinzufügen
				elif bewegung == "Taste 3a":
					print("*" * 30)
					print("Taste 3a")
					#keyboardbefehl hinzufügen		
				time.sleep(pause)
		except KeyboardInterrupt:
			print("Drax: DAMN!")
			pass
	else:
		print("Drax: DAMN!")
		
		
def StartMe():
	befehl = input()
	
	if befehl == "0" or befehl == "???":
		Ende()
	elif befehl == "1" or befehl == "Drax":
		isrun = 1
		Drax(isrun)
	elif befehl == "99" or befehl == "test":
		isrun = 2
		Drax(isrun)
		
		
def Ende():
	print("ByeBye!")
	
	
StartMe()
