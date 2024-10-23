from random import *
import sys

inputfile = open(sys.argv[1], "r")      #Spielerstärken öffnen
raw_input = inputfile.readlines()       #Spielerstärken laden
nPlayers = raw_input[0].strip("\n")     #Anzahl der Spieler laden
raw_input.pop(0)                        #Spieleranzahl aus gelesenem Input entfernen
players = []                            #Leere Spielerliste erstellen
for player in raw_input:                #Für jeden Spieler aus gelesenem Input
    players.append(player.strip("\n"))  #Spieler an die Spielerliste anhängen und formatierungsbedingten Zeilenumbruch entfernen
ligascores = [0]*len(players)           #Liga-Spielstände Liste erstellen mit 0 mit Anzahl der Spieler (für jeden Spieler ein Listenelement)
koscores = [0]*len(players)             #Liga-Spielstände Liste erstellen mit 0 mit Anzahl der Spieler (für jeden Spieler ein Listenelement)
ko5scores = [0]*len(players)            #Liga-Spielstände Liste erstellen mit 0 mit Anzahl der Spieler (für jeden Spieler ein Listenelement)

def fight(dPlayer1,dPlayer2):           #Funktion um zwei Spieler gegeneinander antreten zu lassen
    dTotal = dPlayer1 + dPlayer2        #Gesamtwert berechnen
    dRandom = randint(1,dTotal)         #Zufallszahl zwischen 1 und Gesamtwert generieren
    if(dRandom<=dPlayer1):              #Wenn Zufallszahl kleiner gleich Wert von Spieler 1
        return(1)                       #Hat Spieler 1 gewonnen und der Wert wird zurückgegeben
    else:                               #Wenn die Zahl größer ist,
        return(2)                       #dann hat Spieler 2 gewonnen und der Wert wird zurückgegeben

def LigaMatchMaker(dPlayers):           #Funktion um jedem Spieler seine Gegner zuzuordnen
    dMatches = []                       #Leere Matchliste erstellen
    offset = 1                          #Verschiebungswert auf 1 setzen
    for i in range(len(dPlayers)):      #Für jeden Index der Spieler
        dPlayers.pop(0)                 #Ersten Spieler aus der Liste entfernen
        dOpponents = []                 #Leere Gegnerliste erstellen
        for iO in range(len(dPlayers)): #Für jeden Index (Gegnerindex) aus Spielerliste
            iO += offset                #Zu Gegnerindex die Verschiebung addieren
            dOpponents.append(iO)       #Gegnerindex zu Gegnerliste des Spielers hinzufügen
        dMatches.append(list(dOpponents))   #An Matches, an Index des Spielers, die Liste von Gegnern hinzufügen
        offset += 1                     #Verschiebung um 1 erhöhen
    return(dMatches)                    #Spieler-Gegnerliste zurückgeben

def LigaMatch(dPlayers):                #Funktion um Ligaturnier zu starten
    dscores = [0]*len(dPlayers)         #Leere Liste für Ergebnisse mit Elementen mit 0 mit Anzahl aller Spieler erstellen
    dLigaMatches = LigaMatchMaker(list(dPlayers))   #Matches mit LigaMatchMaker Funktion generieren
    for i in range(len(dLigaMatches)):  #Für jeden Index der Matchliste
        dmatch = dLigaMatches[i]        #Aktuelles Match speichern
        for iOponnent in dmatch:        #Für jeden Index eines Gegners
            if(fight(int(dPlayers[i]),int(dPlayers[iOponnent]))==1):    #Spieler und sein Gegner gegeneinander antreten lassen
                dscores[i] += 1         #Wenn Spieler gewonne hat, Punkt addieren
            else:                       #Wenn Gegner gewonnen hat,
                dscores[iOponnent] += 1 #Punkt für Gegner addieren
    dwinner = dscores.index(max(dscores))   #Höchste Punktzahl und Spieler bestimmen
    return(dwinner)                     #Gewinner zurückgeben

def KoMiniMatch(iPlayers,dPlayers): #Funktion um einzelne Schichten von Turnieren in KO Form durchzuspielen
    counter = 0                     #Zähler null setzen
    dpairs = []                     #Leere Spielerpaar Liste erstellen
    dWinner = []                    #Leere Gewinner Liste erstellen
    while(counter != len(iPlayers)):#Während der Counter nicht so groß ist wie die Anzahl der Spieler
        dpair = [iPlayers[counter],iPlayers[counter+1]] #Paar erstellen, bestehend aus dem Spieler mit dem Index des Counters und den darauffolgenden Spieler
        dpairs.append(list(dpair))      #Einzelnes Paar an Paare anhängen
        counter += 2                    #Counter um 2 erhöhen, dadurch können die paare mit darauffolgendem Spieler erstellt werden
    for imatch in range(len(dpairs)):   #Für Index des Spielerpaares
        dmatch = dpairs[imatch]         #Aktuelles Spielerpaar laden
        dPlayer1 = dmatch[0]            #Spieler 1 laden
        dPlayer2 = dmatch[1]            #Spieler 2 laden
        if(fight(int(dPlayers[dPlayer1]), int(dPlayers[dPlayer2]))==1): #Spieler gegeneinander antreten lassen
            dWinner.append(dPlayer1)    #Wenn Spieler 1 gewonnen hat, Spieler 1 an die Gewinnerliste hinzufügen
        else:                           #Wenn Spieler 2 gewinnen hat,
            dWinner.append(dPlayer2)    #Spieler 2 an die Gewinnerliste hnzufügen
    return(dWinner)                     #Gewinner zurückgeben

def KoMatch(dPlayers):                              #Funktion um ein KO Match zu starten
    iPlayers = [0] * len(dPlayers)                  #Leere Liste mit Elementen mit Anzahl der Spieler mit Inhalt 0 erzeugen
    for iPlayer in range(len(dPlayers)):            #Für jeden Spieler
        iPlayers[iPlayer] = iPlayer                 #Jedem Spieler seinen jeweiligen Index in der Spielerliste zuordnen
    while(1 != len(iPlayers)):                      #Solange die Paare nicht nur 1 sind
        iPlayers = KoMiniMatch(iPlayers,dPlayers)   #Spieler spielen lassen
    return(iPlayers)                                #Gewinner zurückgeben

def Ko5MiniMatch(iPlayers,dPlayers):    #Funktion um einzelne Schichten von Turnieren in KO Form durchzuspielen
    counter = 0                         #Zähler null setzen
    dpairs = []                         #Leere Spielerpaar Liste erstellen
    dWinner = []                        #Leere Gewinner Liste erstellen
    while(counter != len(iPlayers)):    #Während der Counter nicht so groß ist wie die Anzahl der Spieler
        dpair = [iPlayers[counter],iPlayers[counter+1]] #Paar erstellen, bestehend aus dem Spieler mit dem Index des Counters und den darauffolgenden Spieler
        dpairs.append(list(dpair))      #Einzelnes Paar an Paare anhängen
        counter += 2                    #Counter um 2 erhöhen, dadurch können die paare mit darauffolgendem Spieler erstellt werden
    for imatch in range(len(dpairs)):   #Für Index des Spielerpaares
        dmatch = dpairs[imatch]         #Aktuelles Spielerpaar laden
        dPlayer1 = dmatch[0]            #Index von Spieler 1 laden
        dPlayer2 = dmatch[1]            #Index von Spieler 2 laden
        dPlayer1wins = 0                #Gewinne von Spieler 1 auf 0 setzen
        dPlayer2wins = 0                #Gewinne von Spieler 2 auf 0 setzen
        for i in range(5):              #For Schlefe 5 mal ausführen
            if(fight(int(dPlayers[dPlayer1]), int(dPlayers[dPlayer2]))==1): #Spieler gegeneinander antreten lassen, Gewinner des einzelnen Spiels überprüfen
                dPlayer1wins += 1       #Wenn Spieler 1 gewonnen hat, Spieler 1 einen Gewinn hinzufügen
            else:                       #Wenn Spieler 2 gewonne hat
                dPlayer2wins += 1       #Spieler 2 einen Gewinn hinzufügen
        if(dPlayer1wins>dPlayer2wins):  #Wenn Spieler 1 mehr Punkte hat als Spieler 2
            dWinner.append(dPlayer1)    #Spieler 1 an die Gewinner Liste hinzufügen
        else:                           #Wenn Spieler 2 mehr Gewinne hat
            dWinner.append(dPlayer2)    #Spieler 2 an die Gewinner Liste hinzufügen
    return(dWinner)                     #Gewinner zurückgeben

def Ko5Match(dPlayers):                             #Funktion um ein KO Match zu starten
    iPlayers = [0] * len(dPlayers)                  #Leere Liste mit Elementen mit Anzahl der Spieler mit Inhalt 0 erzeugen
    for iPlayer in range(len(dPlayers)):            #Für jeden Spieler
        iPlayers[iPlayer] = iPlayer                 #Jedem Spieler seinen jeweiligen Index in der Spielerliste zuordnen
    while(1 != len(iPlayers)):                      #Solange die Paare nicht nur 1 sind
        iPlayers = Ko5MiniMatch(iPlayers,dPlayers)  #Spieler spielen lassen
    return(iPlayers)                                #Gewinner zurückgeben

for runs in range(int(input("Anzahl der Durchläufe für jede Turnierform: "))):  #In gewünschter Anzahl alle Turniere durchführen
    ligawinner = LigaMatch(players)                 #Ligaturniergewinner herausfinden
    ligascores[ligawinner] += 1                     #Ligaturniergewinner einen Punkt in der Liga-Punkteliste hinzufügen
    kowinner = KoMatch(players)                     #KO-Turiniergewinner herausfinden
    koscores[int(kowinner[0])] += 1                 #KO-Turniergewinner einen Punkt in der KO-Punkteliste hinzufügen
    ko5winner = Ko5Match(players)                   #KO5-Turniergewinner herausfinden
    ko5scores[int(ko5winner[0])] += 1               #KO5-Turniergweinner einen Punkt in der KO5-Punkteliste hinzufügen

ligatotalwinner = ligascores.index(max(ligascores)) #Gesamtgewinner der Ligaturniere ermitteln
kototalwinner = koscores.index(max(koscores))       #Gesamtgewinner der KO-Turniere ermitteln
ko5totalwinner = ko5scores.index(max(ko5scores))    #Gesamtgewinner der KO5-Turniere ermitteln

print("")   #Leere Zeile ausgeben
print("Bei dem Ligaturnier gewann Spieler " + str(ligatotalwinner+1) + " mit Spielerstärke " + str(players[ligatotalwinner]))   #Ergebnis für Ligaturniere ausgeben
print("Bei dem KO-Turnier gewann Spieler " + str(kototalwinner+1) + " mit Spielerstärke " + str(players[kototalwinner]))        #Ergebnis für KO-turniere ausgeben
print("Bei dem KO5-Turnier gewann Spieler " + str(ko5totalwinner+1) + " mit Spielerstärke " + str(players[ko5totalwinner]))     #Ergebnis für KO5-Turniere ausgeben
