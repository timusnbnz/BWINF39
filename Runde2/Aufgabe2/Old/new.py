import sys, os

def comparator(a,b):    #Funktion um dieselben Einträge aus zwei Listen zu finden
    same = []           #Leere Liste wird erstellt, in welcher später alle in beiden Listen vorkommende Elemente gespeichert werden
    for aa in a:            #Für jeden Eintrag in Liste a
        for bb in b:            #Wird jeder Eintrag der Liste b
            if(aa==bb):         #miteinander verglichen
                same.append(aa) #Falls diese gleich sind, wird es der Liste hinzugefügt
    return(same)                #Die Liste mit in beiden Listen vorkommenden Elementen wird zurückgegeben

def allsame(a):         #Funktion um zu überprüfen ob alle Elemente einer Liste gleich sind
    allsame = True      #Variable die Standartmäßig auf True steht, bei nicht gleichen Elemente aber auf False geändert wird
    for aa in a:        #Jedes Element der Liste
        if(not aa==a[0]):   #Wird mit dem ersten Element der Liste verglichen
            allsame = False #Sollten diese nicht gleich sein, wird die Variable auf False gesetzt
            break           #Und der Loop abebrochen
    return(allsame)     #Diese Variable wird dann zurückgegeben

class Spiesse:  #Eine Klasse mit mehreren Funktionen um die verschiedenen Variablen untereinander zu teilen
    def __init__(self,filename):
        inputfile = open(filename,"r")
        rawInput = inputfile.readlines()
        input, self.spiesse, i = [], [], 0
        for rawPiece in rawInput:
            input.append(rawPiece[:-1])
        self.nSorten = int(input[0])
        self.donaldsWunsch = list(filter(None, input[1].split(" ")))
        self.nStalked = int(input[2])
        input.pop(2)
        input.pop(1)
        input.pop(0)
        while(i != (self.nStalked*2)):
            schalen = list(filter(None, input[i].split(" ")))
            sorten = list(filter(None, input[i+1].split(" ")))
            spiess = [schalen,sorten]
            self.spiesse.append(spiess)
            i += 2

    def same(self):
        self.possibilitys = {}
        for spiess1 in self.spiesse:
            for spiess2 in self.spiesse:
                same1 = comparator(spiess1[0],spiess2[0])
                same2 = comparator(spiess1[1],spiess2[1])
                if(not same1 == same2):# "[[],[]]" Herausfiltern
                    for sorte in same2:
                        if(not sorte in self.possibilitys):
                            self.possibilitys[sorte] = []
                        for schale in same1:
                            self.possibilitys[sorte].append(schale)

    def notTogether(self):
        for spiess in self.spiesse:
            for sorte in spiess[1]:
                if(not sorte in self.possibilitys):
                    self.possibilitys[sorte] = []
                for schale in spiess[0]:
                    self.possibilitys[sorte].append(schale)

        for i in range(self.nStalked):
            for sorte in self.possibilitys:
                for schale in self.possibilitys[sorte]:
                    for spiess in self.spiesse:
                        if(schale in spiess[0]):
                            if(not sorte in spiess[1]):
                                while(schale in self.possibilitys[sorte]):
                                    self.possibilitys[sorte].remove(schale)

    def cleaner(self):
        for pair in self.pairs:
            if(pair in self.possibilitys):
                self.possibilitys.pop(pair)
        for possibility in self.possibilitys:
            for pair in self.pairs:
                while(self.pairs[pair] in self.possibilitys[possibility]):
                    self.possibilitys[possibility].remove(self.pairs[pair])

    def combinations(self):
        self.sortedPossibilitys, self.samePossiblitys = {}, []
        for possibility in self.possibilitys:
            for schale in self.possibilitys[possibility]:
                if(not possibility in self.sortedPossibilitys):
                    self.sortedPossibilitys[possibility] = []
                if(not schale in self.sortedPossibilitys[possibility]):
                    self.sortedPossibilitys[possibility].append(schale)
        for possibility in self.sortedPossibilitys:
            for possibility1 in self.sortedPossibilitys:
                if(possibility != possibility1):
                    if(set(self.sortedPossibilitys[possibility]) == set(self.sortedPossibilitys[possibility1])):
                        self.samePossiblitys.append([possibility,possibility1])
        for sames in self.samePossiblitys:
            for sames1 in self.samePossiblitys:
                if(sames != sames1):
                    if(set(sames)==set(sames1)):
                        self.samePossiblitys.remove(sames1)

    def sorter(self):
        self.pairs = {}
        while True:
            last = str(self.possibilitys)+str(self.pairs)
            for possibility in self.possibilitys:
                if(allsame(self.possibilitys[possibility])):
                    self.pairs[possibility] = self.possibilitys[possibility][0]
            self.cleaner()
            if(last==(str(self.possibilitys)+str(self.pairs))):
                self.combinations()
                break

    def donald(self):
        self.donaldsListe = []
        for wunsch in self.donaldsWunsch:
            if not (wunsch in self.pairs or wunsch in self.possibilitys):
                quit("Folgende gewünschte Sorte konnte nicht aus beobachteten Spiessen entnommen werden: \n - " + str(wunsch) + "\nDas Skript wurde abgebrochen")
            if(wunsch in self.pairs):
                self.donaldsListe.append(self.pairs[wunsch])
            for sames in self.samePossiblitys:                      #Alles aus samePossiblitys checken
                if(wunsch in sames):                                #Wenn die Sorte in samePossiblitys ist
                    allinthere = True                               #Preflaggen als wahr
                    for sames1 in sames:                            #
                        if not (sames1 in self.donaldsWunsch):
                            allinthere = False
                            quit("Folgende gewünschte Sorte konnte nicht eindeutig zugeordnet werden:\n - " + str(wunsch) + "\nDas Skript wurde abgebrochen")
                    if(allinthere):
                        for schalen in self.sortedPossibilitys[sames[0]]:
                            self.donaldsListe.append(schalen)
        self.donaldsListe = list(dict.fromkeys(self.donaldsListe))

def main():
    os.system("clear")
    Sp = Spiesse(sys.argv[1])
    Sp.same()
    Sp.notTogether()
    Sp.sorter()
    Sp.donald()
    if(len(Sp.donaldsListe)==len(Sp.donaldsWunsch)):
        print("Für Donalds Wunschspiess müssen folgende Schalen gewählt werden:")
        outputstring = ""
        for entry in Sp.donaldsListe:
            outputstring += entry + ", "
        outputstring = outputstring[:-2]
        print(outputstring)
    else:
        quit("Es konnten nicht alle erwünschten Schalen bestimmt werden.")
main()
