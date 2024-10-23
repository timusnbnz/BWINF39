from random import *        #Importieren der "random" Bibliothek
password = ""               #Leerer Passwort String, an den später einzelne Zeichen angehängt werden
last_char = 0               #Letztes in Passwort geschriebenes Zeichen, da noch keines vergben wurde, ist es 0
wished_chars = 0            #Anzahl an erwünschten Zeichen für Passwort
while(wished_chars<8):      #Solange gewünschte Zeichen nicht mindestens 8 sind
    wished_chars = int(input("Anzahl an  Zeichen des Passworts (min.8): "))  #Abfrage nach gewünschter Länge

def generatepwd(caps,numbers,extra):    #Funktion für Zeichengenerator mit extra Attributen für Großbuchstaben, Zahlen und Sonderzeichen
    given_chars = "abcdefghijklmnopqrstuvwxyz"  #Standardauswahl an Zeichen, in diesem Fall nur Kleinbuchstaben
    if(caps):                                   #Wenn Großbuchstaben erwünscht sind
        given_chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Anfügen von Großbuchstaben an den vorgegebenen String
    if(numbers):                                #Wenn Zahlen erwünscht sind
        given_chars = "1234567890"              #String an möglichen Zeichen wird durch Zahlen ersetzt
    if(extra):                                  #Wenn Sonderzeichen gewünscht sind
        given_chars = "!?.#"                    #String mit möglichen Zeichen wird durch Sonderzeichen ersetzt
    random = randint(0,len(given_chars)-1)      #Eine zufällige Zahl zwischen 0 und der Länge -1 der möglichen Zeichen wird erzeugt
    return(given_chars[random])                 #Aus dem String mit möglichen Zeichen wird das Zeichen mit der Position "random", welche zufällig generiert wurde, entnommen

while not (wished_chars==0):                    #Passworterzeugungsschleife: Solange nicht genug Zeichen generiert wurden
    if(wished_chars<=3 and wished_chars>1):     #Wenn das Zeichen das 3. letzte oder kleiner, aber größer als 0 ist (also 3. oder 2. letztes)
        char = generatepwd(False,True,False)    #Zufälliges Zeichen ohne Großbuchstaben, nur aus Zahlen und kein Sonderzeichen wird generiert
    elif(last_char == 0):                       #Wenn es das erste Zeichen des Passwortes ist (last_char noch bei vordefiniertem Wert, also nicht geändert)
        char = generatepwd(True,False,False)    #Zufälliges Zeichen mit Großbuchstaben (und Kleinbuchstaben), aber weder aus Zahlen noch Sonderzeichen wird generiert
    elif(wished_chars==1):                      #Wenn es letzes Zeichen des Passwortes ist
        char = generatepwd(False,False,True)    #Zufälliges Zeichen nur aus Sonderzeichen wird generiert
    else:                                       #Wenn es keines der Bedingung betrifft
        char = generatepwd(False,False,False)   #Zufälliges Zeichen nur aus Kleinbuchstaben wird generiert
    if(last_char != char):                      #Wenn das generierte Zeichen nicht gleich dem letzen Zeichen ist
        last_char = char                        #Das generierte Zeichen wird zum letzen Zeichen
        password = password + char              #An den vorhandenen Passwort String wird das generierte Zeichen angehängt
        wished_chars -= 1                       #Die Zahl an zu generierenden Zeichen wird um 1 verringert und somit heruntergezählt

print("Generiertes Passwort:")                  #"Generiertes Passwort:" wird ausgegeben
print(password)                                 #Das generierte Passwort wird ausgegeben
