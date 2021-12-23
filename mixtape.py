import time
import keyboard

#Keybinding in FFXIV
##Global##


def Lieder():
    #Die Liederliste gibt die Lieder und Noten wieder. Es können neue Lider hinzugefügt werden am ende indem man ', "Liedname" : [[Noten1,Zeit],[Note2,Zeit]]' dahinter schriebt. die {} müssen eine am anfang und eine am ende sein.
    Liederliste = {
    "Testlied" : [["A1",0.25],["C2",0.2],["D2",0.3],["leer",0.2],["D2",0.25],["leer",0.25],["D2",0.22],["leer",0.1],["E2",0.25],["F2",0.3],["leer",0.2],["F2",0.25],["leer",0.2],["F2",0.25],["G2",0.25],
    ["E2",0.25],["leer",0.25],["E2",0.45],["leer",0.125],["D2",0.25],["C2",0.2],["leer",0.125],["C2",0.25],["D2",0.55],["leer",0.4],["A1",0.25],["C2",0.2],["D2",0.3],["leer",0.2],["D2",0.25],["leer",0.25],["D2",0.22],
    ["leer",0.1],["E2",0.25],["F2",0.3],["leer",0.2],["F2",0.25],["leer",0.2],["F2",0.25],["G2",0.25],["E2",0.25],["leer",0.25],["E2",0.45],["leer",0.125],["D2",0.25],["C2",0.2],["leer",0.125],["C2",0.25],["D2",0.65],
    ["leer",0.35],["A1",0.25],["C2",0.2],["D2",0.3],["leer",0.2],["D2",0.25],["leer",0.25],["D2",0.22],["leer",0.1],["F2",0.25],["G2",0.3],["leer",0.2],["G2",0.2],["leer",0.3],["G2",0.2],["leer",0.125],["A2",0.2],
    ["Bb",0.3],["leer",0.2],["Bb",0.25],["leer",0.2],["A2",0.2],["leer",0.05],["G2",0.25],["A2",0.2],["D2",0.6],["leer",0.2],["D2",0.25],["E2",0.25],["F2",0.35],["leer",0.2],["F2",0.35],["leer",0.15],["G2",0.45],
    ["A2",0.2],["D2",0.6],["leer",0.2],["leer",0.1],["F2",0.2],["E2",0.33],["leer",0.1],["E2",0.45],["leer",0.1],["F2",0.2],["leer",0.1],["D2",0.25],["E2",0.55]],
    
    "Gigi D'Agostino" : [["Ff2",0.25],["leer",0.25],["Ff2",0.25],["leer",0.25],["Ff2",0.25],["leer",0.25],["Ff2",0.25],["leer",0.04],["D3",0.25],["leer",0.04],["Cc3",0.25],["leer",0.25],["Cc3",0.25],["leer",0.25],
    ["Cc3",0.25],["leer",0.25],["Cc3",0.25],["leer",0.05],["D3",0.25],["leer",0.075],["H2",0.25],["leer",0.25],["H2",0.25],["leer",0.25],["H2",0.25],["leer",0.25],["H2",0.25],["leer",0.03],
    ["A2",0.25],["leer",0.15],["H2",0.25],["leer",0.2],["H2",0.25],["leer",0.2],["H2",0.25],["leer",0.05],["A2",0.25],["leer",0.1],["H2",0.25],["leer",0.1],["A2",0.25],["leer",0.1],["Ff2",0.25],["leer",0.25],
    ["Ff2",0.25],["leer",0.25],["Ff2",0.25],["leer",0.25],["Ff2",0.25],["leer",0.04], ["D3",0.25],["leer",0.04],["Cc3",0.25],["leer",0.25],
    ["Cc3",0.25],["leer",0.25],["Cc3",0.25],["leer",0.25],["Cc3",0.25],["leer",0.05], ["D3",0.25],["leer",0.075],["H2",0.25],["leer",0.25],["H2",0.25],["leer", 0.25],["H2",0.25],
    ["leer",0.25],["H2",0.25],["leer",0.03],["A2",0.25],["leer",0.15],["H2",0.25],["leer",0.2],["H2",0.25],["leer",0.2],["H2",0.25],["leer",0.05],["A2",0.25],["leer",0.075],["H2",0.25],
    ["leer",0.075],["A2",0.25],["leer",0.1],["Ff2",0.25]],

    "Jingle Bells" : [["C3",0.4],["leer",0.075],["C3",0.4],["leer",0.075],["C3",0.4],["leer",0.275],["C3",0.15],["leer",0.075],["C3",0.4]]
    }

    #Liste zur auswahl des Liedes
    print("\n\n\nchoose you favorit?\n")
    liednr = 0
    liedernamen = []
    for key in Liederliste:
        liednr += 1
        liedernamen.append(key)
        print(f"Nr.{liednr}: {key}")

    liednummer = input()
    print("\n\nWartezeit zum wechseln von 5Sekunden.....GO GO GO")
    time.sleep(1)
    Mixtapeplayer(Liederliste[liedernamen[int(liednummer)-1]])

    
def Mixtapeplayer(Testlied):
    #Play from liederliste
    notenliste = [["C1","q"],["D1","w"],["E1","e"],["F1","r"],["G1","t"],["A1","z"],["H1","u"],["C2","i"],["D2","o"],["E2","p"],["F2","<"],["G2","y"],["A2","x"],["H2","c"],["C3","v"],["D3","b"],
    ["E3","n"],["F3","m"],["G3",","],["A3","."],["H3","-"],["Cc1","2"],["Eb1","3"],["Ff1","5"],["Gg1","6"],["Hb1","7"],["Cc2","9"],["Eb2","0"],["Ff2","a"],["Gg2","s"],["Hb2","d"],["Cc3","g"],["Eb3","h"],
    ["Ff3","k"],["Gg3","l"],["Hb3","l"],["Bb","d"]]

    itr = iter(Testlied)

    for note in Testlied:
        if note[0] == "leer":
            time.sleep(note[1])
            print(f"sleep {note[1]}")
        else:   
            for each in notenliste:
                if note[0] == each[0]:
                    print(each[1])
                    keyboard.press(each[1])
                    time.sleep(note[1])
                    keyboard.release(each[1])
    print("Ende")

    #Für Testzwecke der Instrumentenwechsel
    #Instrumentwechsel()


def Instrumentwechsel():
    keyboard.press("esc")
    time.sleep(0.01)
    keyboard.release("esc")
    time.sleep(0.15)
    keyboard.press("2")
    time.sleep(0.01)
    keyboard.release("2")
    Lieder()


def Menue():
    print("\n\nNochmal?(j/n)")
    if input() == "j":
       Lieder()    