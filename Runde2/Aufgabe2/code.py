import sys
import os

os.system("clear")
#Datei öffnen und lesen
filename = sys.argv[1]
file = open(filename)
content = file.readlines()
#Inhalt lesen
anzahlsorten = content[0]
wunschsorten = content[1]
anzahlbeobachtet = content[2]
anzahlbeobachtet = int(anzahlbeobachtet)
#Leere Variablen definieren
pairs = {}
groups = []
skewers = []
#Debug print
def debug(output):
    print(output)
#Spiesse lesen
for i in range(anzahlbeobachtet):
    i = 3 + i*2
    skewer = [var for var in content[i][:-1].split(" ") if var], [var for var in content[i+1][:-1].split(" ") if var]
    skewers.append(skewer)
#Leeres Dictonary für Sorten erstellen
for skewer in skewers:
    for sorte in skewer[1]:
        pairs[sorte] = ""
#Alle Spiesse zeigen
debug("----Spiesse---")
for skewer in skewers:
    string = ""
    for number in skewer[0]:
        string = string + number + " "
    string = string + ": "
    for sorte in skewer[1]:
        string = string + sorte + " "
    debug(string)
debug("----Gruppen---")
#Funktion 1: Gleiche Einträge aus zwei Listen finden
def occuring(list1, list2):
    finallist = []
    for entry1 in list1:
        for entry2 in list2:
            if(entry1==entry2):
                finallist.append(entry1)
    return(finallist)
###Hauptteil
#Gleichzeitig Vorkommende Schalen und Sorten
for skewer1 in skewers:
    for skewer2 in skewers:
        if(skewer1 != skewer2):
            group = [occuring(skewer1[0],skewer2[0]),occuring(skewer1[1],skewer2[1])]
            if(group != [[],[]]):
                groups.append(group)
#Alle Gruppen anzeigen
for group in groups:
    debug(group)
#Bereits alleine vorkommende Sorten filtern
for i in range(len(groups)):
    group = groups[i]
    if(len(group[0])==1):
        pairs[group[1][0]] = group[0][0]
#Bisherige Ergebnisse
debug("-Bisherige Paare-")
for pair in pairs:
    debug(pair + " -> " + pairs[pair])
