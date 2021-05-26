import random as rand

# globale Variablen
print("Bitte geben Sie die Göße des Spielfelds ein: ")
groesse_spielfeld = int(input())

# COINFLIP FÜR RUNDENSTART
def Ermittlung_Rundenstart():
    spieler_coin = input("Kopf oder Zahl? : ")

    # Kopf hat den Wert 0 und Zahl hat den Wert 1. Wenn der Spieler
    # Kopf oder Zahl schreibt und der Wert ebenfalls übereinstimmt, 
    # dann darf der Spieler anfangen. Ansonsten setzt der PC 
    # automatisch sein Zeichen.

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
    
# BIBLIOTHEK FÜR DIE SPIELFIGUREN
def dict_values():
    werte_zeichen = {"O" : 0,
                     "X" : 1}
    return werte_zeichen

# INITIALISIERUNG GRÖßE FELD
def init_x_header(x):
    init_x = {}
    for i in range(x):
        init_x[i] = " "
    return init_x

# SLIDER ZUR ÜBERPÜFUNG DER REGELN
def slider(n, dict_zeichen):
    liste_zeichen = list(dict_zeichen)
    liste_idx = 0
    req_erfuellt = [False, dict_zeichen]

    for key in dict_values().keys():
        desc = 1
        # Überprüfung horizontal
        for i in range(n):
            for x in range(i*n, ((i+1)*n)):
                if liste_zeichen[x] == key:
                    liste_idx = liste_idx+1
                    if liste_idx == n:
                        liste_idx = 0
                        req_erfuellt[0] = True
                        req_erfuellt[1] = key
                        break
                else:
                    liste_idx = 0
                    break

        # überprüfung vertikal
        for i in range(n):
            for j in range(n):
                if liste_zeichen[(j*n)+i] == key:
                    liste_idx = liste_idx+1
                if liste_idx == n:
                    liste_idx = 0
                    req_erfuellt[0] = True
                    req_erfuellt[1] = key
                    break
            else:
                liste_idx = 0
                break

        # Überprüfung diagonal nach rechts
        for i in range(n):
            if liste_zeichen[(i*n)+i] == key:
                liste_idx = liste_idx+1
                if liste_idx == n:
                    liste_idx = 0
                    req_erfuellt[0] = True
                    req_erfuellt[1] = key
                    break
            else:
                liste_idx = 0
                break

        # Überprüfung diagonal nach links
        for i in range(n):                
            if liste_zeichen[((i+1)*n)-desc] == key:
                liste_idx = liste_idx+1
                if liste_idx == n:
                    liste_idx = 0
                    req_erfuellt[0] = True
                    req_erfuellt[1] = key
                    break
            else:
                liste_idx = 0
                break
            desc = desc + 1

    # Es wird eine Liste zurückgegeben, die an der vordersten
    # Stelle einen boolschen und an der hinteren Stelle ein
    # Zeichen der Bibliothek enthält. So wird festgestellt, 
    # ob die Bedingung für den Spieler oder für den Computer 
    # erfüllt wurde.

    return req_erfuellt   

# INITIALISIERUNG DES SPIELS, BZW DES FELDES
def map(x, y):

    # Es wird zunächst das Feld erstellt. Da das Feld aus n
    # Reihen und n Spalten bestehen soll, soll die Liste
    # des Felds eine Größe von n*n haben, die dann später
    # gleichmäßig verteilt wird. 
    # 
    # Es werden außerdem die lokale Variablen initialisiert.

    map_x = init_x_header(x * y)
    wechsel = False
    runde = True
    runde_spieler = False
    runde_computer = False
    
    # Hier wird geschaut, wer mit dem Spielen anfängt.

    if Ermittlung_Rundenstart() == True:
        wechsel = False
        runde_spieler = True
    else:
        wechsel = True
        runde_computer = True

    # Initialisierung der Werte aus der Bibliothek, damit
    # sie verständlicher sind
    for key, value in dict_values().items():
        if value == 0:
            key_spieler = key
        if value == 1:
            key_computer = key

    # Rundenstart
    while runde:

        # Es wird jedes Mal am Anfang der Runde geschaut, ob jemand
        # gewonnen hat. 
        if slider(x, map_x.values())[0] == True:
            for i in range(0, y):
                print(list(map_x.values())[(i*y):((i+1)*y)])
            runde = False
            if(slider(x, map_x.values())[1] == key_spieler):
                print("Der Spieler hat gewonnen\n")
            else: 
                print("Der Computer hat gewonnen\n")
            break
        
        # Wenn der Computer seinen Zug gemacht hat, so
        # ist dann der Spieler dran.
        if wechsel == False:
            print("Wo möchten Sie Ihr Zeichen setzen? : ")
            ziel = int(input())
            
            # Hier wird das Zeichen vom Spieler in das ausgewählte
            # Feld eingesetzt. Hierbei wird von 1 und nicht von 0 hochgezählt,
            # damit das Spiel verstänlicher ist.
            while runde_spieler:
                if ziel <= len(map_x):

                    # Sofern das ausgewählte Feld nicht besetzt ist, wird das Zeichen in das
                    # Feld eingesetzt, ansonsten muss der Spieler erneut auswählen.
                    if map_x[ziel-1] != key_computer and map_x[ziel-1] != key_spieler:
                        map_x[ziel-1] = key_spieler
                        wechsel = True
                        runde_spieler = False
                        runde_computer = True
                    else:
                        print("Bitte versuchen Sie es nochmal!")
                        break

                # Die, vom Spieler angegebene Zahl muss natürlich von 1 bis n^n sein,
                # sonst liegt sie außerhalb der Liste des Spielfelds
                else:
                    print("Bitte eine gültige Zahl zwischen 1 und " + str(len(map_x)) + " angeben")
                    break

        else:
            print("Computer: ")
            
            # Der Computer schaut sich die Liste an und wählt ein Feld aus,
            # das weder vom Spieler noch von sich selbst belegt ist.
            while runde_computer:
                i = rand.randint(1, len(map_x)-1)
                if map_x[i] != key_spieler and map_x[i] != key_computer:
                    map_x[i] = key_computer
                    runde_computer = False

            # Nach der Runde wird gewechselt.
            wechsel = False
            runde_spieler = True
            for i in range(0, y):
                print(list(map_x.values())[(i*y):((i+1)*y)])

# Hier wird das Spielfeld mit der angegebenen Größe erstellt
# und ausgeführt.
def Spiel():
    n = groesse_spielfeld
    map(n, n)

Spiel()