import sys
import time

starttime = time.time()

file = open(sys.argv[1])
content = file.readlines()
umfang = int(content[0].split(" ")[0])
anzahladressen = int(content[0].split(" ")[1][:-1])
adressen = content[1].strip().split(" ")
halberumfang = umfang/2
halbeadressen = anzahladressen/2
bestdistances = [umfang]*anzahladressen
bestpositions = [0,0,0]
counter = 0
ohshitthereisanotherone = False

def main():
    global umfang, anzahladressen, adressen, halberumfang, halbeadressen, bestdistances, bestpositions, counter, ohshitthereisanotherone
    for bigcounter in range(2):
        for a in range(umfang):
            for b in range(a+1,umfang):
                for c in range(b+1,umfang):
                    currentdistances, votes, redflag = [], 0, False
                    for i in range(anzahladressen):
                        adresse = int(adressen[i])
                        if(adresse==a or adresse==b or adresse==c):
                            redflag = True
                            break
                        aa = abs(a-adresse)
                        bb = abs(b-adresse)
                        cc = abs(c-adresse)
                        aaa = umfang-aa
                        bbb = umfang-bb
                        ccc = umfang-cc
                        currentdistance = min([aa,bb,cc,aaa,bbb,ccc])
                        currentdistances.append(currentdistance)
                        if(currentdistance<bestdistances[i]):
                            votes += 1
                        if()
                    counter += 1
                    if(votes>halbeadressen and redflag==False):
                        bestvotes = votes
                        bestpositions = [a,b,c]
                        bestdistances = currentdistances
                        if(bigcounter==1):
                            ohshitthereisanotherone = True
                            return()
main()

if not (ohshitthereisanotherone):
    print("Stabiler Standort konnte gefunden werden")
    print(bestpositions)
else:
    print("Es konnte kein Stabiler Standort gefunden werden")

endtime = time.time()
print("\n" + str(counter) + " Operationen in " + str(round(endtime-starttime,2)) + "s")
print(str(round(counter/(endtime-starttime),2)) + " Operationen pro Sekunde")
