import random as rng
import keyboard
import time
import mixtape
from datetime import datetime


print(" _______  .______        ___      ___   ___    .______   ____    ____           __   _  _      _______   _______  ____    _______  ")
print("|       \ |   _  \      /   \     \  \ /  /    |   _  \  \   \  /   /          |  | | || |    /  _____| /  _____||___ \  |       \ ")
print("|  .--.  ||  |_)  |    /  ^  \     \  V  /     |  |_)  |  \   \/   /           |  | | || |_  |  |  __  |  |  __    __) | |  .--.  |")
print("|  |  |  ||      /    /  /_\  \     >   <      |   _  <    \_    _/      .--.  |  | |__   _| |  | |_ | |  | |_ |  |__ <  |  |  |  |")
print("|  '--'  ||  |\  \-. /  _____  \   /  .  \     |  |_)  |     |  |        |  `--'  |    | |   |  |__| | |  |__| |  ___) | |  '--'  |")
print("|_______/ | _| `.__|/__/     \__\ /__/ \__\    |______/      |__|         \______/     |_|    \______|  \______| |____/  |_______/ \n\n")
                                                                                                                                      

print("How is invisible?")
print("1. Drax")
print("0. ???")
print("Musik or m")

isrun = 0


def Drax(isrun):
	optionen = ["Taste 1a", "Taste 2a", "Taste 3a"]
	zeit = [1, 2, 5, 15, 20, 30]
	runs = 0
	
	if isrun == 2:
		print(f"Drax TEST-movement @{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
		try:
			while isrun == 2:
				print("*" * 30)
				runs += 1
				print(f"movementframe {runs} @{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
				print(rng.choice(optionen))
				pause = rng.choice(zeit)
				print(f"Wartezeit: {pause}")
				time.sleep(pause)
		except KeyboardInterrupt:
			print("Drax: DAMN!")
			pass
	elif isrun == 1:
		print(f"Drax incedible movement start @{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
		try:
			while isrun == 1:
				pause = rng.choice(zeit)
				bewegung = rng.choice(optionen)
				if bewegung == "Taste 1a":
					print("*" * 30)
					runs += 1
					print(f"movementframe {runs} @{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
					print("Taste 1a")
					keyboard.press('s')
					time.sleep(1)
					keyboard.release('s')
					print(f"next frame in {pause}sec")
					time.sleep(pause)
				elif bewegung == "Taste 2a":
					print("*" * 30)
					runs += 1
					print(f"movementframe {runs} @{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
					print("Taste 2a")
					keyboard.press('w')
					time.sleep(1)
					keyboard.release('w')
					print(f"next frame in {pause}sec")
					time.sleep(pause)
				elif bewegung == "Taste 3a":
					print("*" * 30)
					runs += 1
					print(f"movementframe {runs} @{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
					print("Taste 3a")
					keyboard.press('a')
					time.sleep(1)
					keyboard.release('a')
					print(f"next frame in {pause}sec")
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
	elif befehl == "musik" or befehl == "m":
		mixtape.Lieder()
		
		
def Ende():
	print("ByeBye!")
	
	
StartMe()
