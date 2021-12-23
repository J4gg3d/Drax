import time
import keyboard

#Keybinding in FFXIV
##Global##


def Lieder():
    Testlied = [["A1",0.25],["C2",0.2],["D2",0.3],["leer",0.2],["D2",0.25],["leer",0.25],["D2",0.22],["leer",0.1],["E2",0.25],["F2",0.3],["leer",0.2],["F2",0.25],["leer",0.2],["F2",0.25],["G2",0.25],
    ["E2",0.25],["leer",0.25],["E2",0.45],["leer",0.125],["D2",0.25],["C2",0.2],["leer",0.125],["C2",0.25],["D2",0.55],["leer",0.4],["A1",0.25],["C2",0.2],["D2",0.3],["leer",0.2],["D2",0.25],["leer",0.25],["D2",0.22],
    ["leer",0.1],["E2",0.25],["F2",0.3],["leer",0.2],["F2",0.25],["leer",0.2],["F2",0.25],["G2",0.25],["E2",0.25],["leer",0.25],["E2",0.45],["leer",0.125],["D2",0.25],["C2",0.2],["leer",0.125],["C2",0.25],["D2",0.65],
    ["leer",0.35],["A1",0.25],["C2",0.2],["D2",0.3],["leer",0.2],["D2",0.25],["leer",0.25],["D2",0.22],["leer",0.1],["F2",0.25],["G2",0.3],["leer",0.2],["G2",0.2],["leer",0.3],["G2",0.2],["leer",0.125],["A2",0.2],
    ["Bb",0.3],["leer",0.2],["Bb",0.25],["leer",0.2],["A2",0.2],["leer",0.05],["G2",0.25],["A2",0.2],["D2",0.6],["leer",0.2],["D2",0.25],["E2",0.25],["F2",0.35],["leer",0.2],["F2",0.35],["leer",0.15],["G2",0.45],
    ["A2",0.2],["D2",0.6],["leer",0.2],["leer",0.1],["F2",0.2],["E2",0.33],["leer",0.1],["E2",0.45],["leer",0.1],["F2",0.2],["leer",0.1],["D2",0.25],["E2",0.55]]
    print("\n\n\nchoose you favorit?\n")
    Liednr = 0

    for each in liederliste:
        Liednr += 1
        print(f"Nr.{Liednr}: {each}")

    #für den Test:
    Mixtapeplayer(Testlied)

    
def Mixtapeplayer(Testlied):
    #Play from liederliste
    notenliste = [["C1","z"],["D1","u"],["E1","i"],["F1","o"],["G1","p"],["A1","a"],["H1","s"],["C2","9"],["D2","0"],["E2","q"],["F2","w"],["G2","e"],["A2","r"],["H2","t"],["C3","1"],["D3","2"],
    ["E3","3"],["F3","4"],["G3","5"],["A3","6"],["H3","7"],["C+1","8"],["Bb","j"]]

    print("\n\nWartezeit zum wechseln von 5Sekunden.....GO GO GO")
    time.sleep(0.5)
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
    Instrumentwechsel()


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