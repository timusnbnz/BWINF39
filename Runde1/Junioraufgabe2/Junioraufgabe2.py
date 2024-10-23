import sys

inputfile = open(sys.argv[1],"r")               #Laden der Karte
raw_input = inputfile.readlines()               #Einlesen der Karte
width = int(raw_input[0])                       #Breite auslesen
height = int(raw_input[1])                      #Höhe auslesen
raw_input.pop(0)                                #Zeile 1 aus Array löschen
raw_input.pop(0)                                #Zeile 2 aus Array löschen
map = []                                        #Leere Karte erzeugen
bauten = 0                                      #Bautenvariable erzeugen
for i in range(len(raw_input)):                 #Für jede Zeile der rohen Daten
    y_raw = raw_input[i]                        #Zeile auslesen und speichern
    y_raw = list(y_raw[:-1])                    #Gespeicherte Zeile zu Array und Zeilenumbruch entfernen
    map.append(y_raw)                           #Gespeicherte Daten zur Karte hinzufügen

def check(dx,dy):                               #Funktion zum überprüfen ob ein X an Position mit Koordinaten x und y ist
    dYaxis = map[dy]                            #Komplette y-Achse aus Karte auslesen
    dPoint = dYaxis[dx]                         #Punkt mit x Koordinate aus der y-Achse entnehmen
    if(dPoint=="X"):                            #Wenn der Punkt ein "X" ist
        return(True)                            #True zurückgeben
    else:                                       #Ansonsten
        return(False)                           #False zurückgeben

def bau(dx,dy):                                 #Funktion zum überprüfen ob an einer x- und y- Koordinate ein Bau vorhanden ist
    if(check(dx,dy)==check(dx+1,dy)==check(dx+2,dy)==check(dx,dy+1)==check(dx,dy+2)==check(dx,dy+3)==check(dx+2,dy+1)==check(dx+2,dy+2)==check(dx+2,dy+3)==check(dx+1,dy+3)==True) and (check(dx+1,dy+1)==check(dx+1,dy+2)==False): #Mit der check Funktion überprüfen ob ein Punkt die Form eines Baus hat
        return(True)                            #True zurückgeben wenn Form eines Baus vorhanden ist
    else:                                       #Ansonsten
        return(False)                           #False zurückgeben

for x in range(width-2):                        #Für jede x-Koordinate in Breite -2 (Somit nicht out of range der Karte)
    for y in range(height-3):                   #Für jede y-Koordinate in Höhe -3 (Somit nicht out of range der Karte)
        if(bau(x,y)):                           #Überprüfen ob an diesem Punkt ein Bau vorhanden ist
            bauten +=1                          #Bauten-Zähler erhöhen
print("Anzahl der Bauten: " + str(bauten))      #Anzahl der Bauten ausgeben
