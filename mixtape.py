import time
import keyboard

#Keybinding in FFXIV
##Global##


def Lieder():
    liederliste = [["A1","C1","D1"],["D", "C", "B", "A"]]
    Testlied = [["A1",0.25],["C2",0.25],["D2",0.5],["leer",0.5],["D2",0.25],["leer",0.5],["D2",0.25],["E2",0.5],["F2",0.5],["leer",0.25],["F2",0.5],["leer",0.25],["F2",0.5],["G2",0.5],["E2",0.5],["leer",0.25],
    ["E2",1]]
    print("\n\n\nchoose you favorit?\n")
    Liednr = 0

    for each in liederliste:
        Liednr += 1
        print(f"Nr.{Liednr}: {each}")

    #für den Test:
    Mixtapeplayer(Testlied)

    
def Mixtapeplayer(Testlied):
    #Play from liederliste
    notenliste = [["C1","1"],["D1","2"],["E1","3"],["F1","4"],["G1","5"],["A1","6"],["H1","7"],["C+1","8"],["C2","9"],["D2","0"],["E2","q"],["F2","w"],["G2","e"],["A2","r"],["H2","t"],["C3","z"],["D3","u"],
    ["E3","i"],["F3","p"],["G3","p"],["A3","a"],["H3","s"]]

    print("\n\nWartezeit zum wechseln von 5Sekunden.....GO GO GO")
    time.sleep(5)
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


