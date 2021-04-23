# Willkommen in meinem Tic-Tac-Toe Spiel [das nie endet]
# 
# Die Regeln sind einfach:  -Wähle eine Zahl zwischen 1 und 9 
#                           -Wenn die Zahl größer oder gleich groß ist, wie die, 
#                            von dem Computer, dann fangen Sie an. Ansonsten der PC
#                           -Die Kacheln sind durchnummeriert (1- 2^n) und man wählt
#                            eine beliebige Zahl aus, die dann entsprechend durch das 
#                            eigene Zeichen belegt wird
#                           -Sobald man n konsequente Zeichen hat, gewinnt man... oder so...
#                           -Wenn man sich am Anfang des Spieles verschreibt,
#                            dann fängt der Computer automatisch an :D
#
# Viel Spaß und vor allem, viel Erfolg

# Funktionen im Hauptmodul
#  - Ermittlung des Spielstartes
#  - Erste Schrite
#  - Rundenwechsel
#  - Stand nach jeder Runde anzeigen
#  - Erweiterung  
#
#  - Neue Runde, wenn man abbrechen will

import random as rand

# globale Variablen
print("Bitte geben Sie die Göße des Spielfelds ein: ")
groesse_spielfeld = int(input())

def Ermittlung_Rundenstart():
    spieler_coin = input("Kopf oder Zahl? : ")

    if spieler_coin == "Kopf" and (rand.randint(0, 1)) == 0:
        print("Es ist Kopf. Sie fangen an!!!")
        spieler_start = True

    elif spieler_coin == "Zahl" and (rand.randint(0, 1)) == 1:
        print("Es ist Zahl. Sie fangen an!!!")
        spieler_start = True

    else:
        print("Leider kein(e) " + spieler_coin + ". Der Computer fängt an!!!")
        spieler_start = False

    return spieler_start
    
def dict_values():
    werte_zeichen = {"O" : 0,
                     "X" : 1,
                     "_" : 2}
    return werte_zeichen

def init_x_header(x):
    for key, value in dict_values().items():
        if value == 2:
            zeichen_neutral = key
    init_x = {}
    for i in range(x):
        init_x[i] = zeichen_neutral
    return init_x

def slider(n, dict_zeichen):
    liste_zeichen = list(dict_zeichen)
    liste_idx = 0
    req_erfuellt = False

    # Muss alle Regeln von Tic-Tac-Toe verfolgen 
    for key in dict_values().keys():
        if key != "_":
            desc = 1
            for i in range(0, n):
                desc = 1
                for x in range(i*n, ((i+1)*n)):
                    if liste_zeichen[x] == key:
                        liste_idx = liste_idx+1
                        if liste_idx == n:
                            liste_idx = 0
                            req_erfuellt = True
                            break
                    else:
                        liste_idx = 0
                        break

                if liste_zeichen[((i+1)*n)-desc] == key or liste_zeichen[i*n] == key or liste_zeichen[(i*n)+i] == key:
                    liste_idx = liste_idx+1
                    if liste_idx == n:
                        liste_idx = 0
                        req_erfuellt = True
                        break
                else:
                    liste_idx = 0
                    break
                desc = desc + 1
        else:
            continue

    return req_erfuellt   

def map(x, y):
    runde = True
    map_x = init_x_header(x * y)
    wechsel = False
    runde_spieler = False
    runde_computer = False
    
    if Ermittlung_Rundenstart() == True:
        runde_spieler = True
    else:
        runde_computer = True

    for key, value in dict_values().items():
        if value == 0:
            key_spieler = key
        if value == 1:

            key_computer = key

    while runde:
        if slider(x, map_x.values()) == True:
            runde = False
            print("Herzlichen Glückwunsch, Sie haben gewonnen!\n")
            break

        if wechsel == False:
            print("Wo möchten Sie Ihr Zeichen setzen? : ")
            ziel = int(input())
            

            while runde_spieler:
                if map_x[ziel-1] != key_computer and map_x[ziel-1] != key_spieler:
                    if ziel <= len(map_x):
                        map_x[ziel-1] = key_spieler
                        wechsel = True
                        runde_spieler = False
                        runde_computer = True
                    else:
                        print("Bitte eine gültige Zahl zwischen 0 und " + str(len(map_x-1)) + " angeben")
                        break
                else:
                    print("Bitte versuchen Sie es nochmal!")
                    break
                
        for i in range(0, y):
            print(list(map_x.values())[(i*y):((i+1)*y)], flush=True)

        else:
            print("Computer: ")
            while runde_computer:
                i = rand.randint(1, len(map_x)-1)
                if map_x[i] != key_spieler and map_x[i] != key_computer:
                    map_x[i] = key_computer
                    runde_computer = False

            wechsel = False
            runde_spieler = True
            for i in range(0, y):
                print(list(map_x.values())[(i*y):((i+1)*y)])

def Spiel():
    n = groesse_spielfeld
    map(n, n)

Spiel()