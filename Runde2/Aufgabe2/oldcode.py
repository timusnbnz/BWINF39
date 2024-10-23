import sys

groups = []
skewers = []
identified = {}

file = open(sys.argv[1])
content = file.readlines()

nobstsorten = content[0]
wunschsorten = content[1]
nbeobachtet = int(content[2])

def listcompare(list1,list2):
    same = []
    for entry1 in list1:
        for entry2 in list2:
            if(entry1==entry2):
                same.append(entry1)
    return(same)

for i in range(nbeobachtet):
    i = 3+(i*2)
    a = [var for var in content[i][:-1].split(" ") if var], [var for var in content[i+1][:-1].split(" ") if var]
    skewers.append(a)
#Ende von Startup
def findoccuring():
    for skewer1 in skewers:
        for skewer2 in skewers:
            if(skewer1 != skewer2):
                a = [listcompare(skewer1[0],skewer2[0]),listcompare(skewer1[1],skewer2[1])]
                if (a != [[],[]]):
                    groups.append(a)

def findallfruits():
    for skewer in skewers:
        for fruit in skewer[1]:
            identified[fruit] = ""

def purge():
    for id in identified:
        i = 0
        for group in groups:
            while(str(identified[id]) in group[0]):
                group[0].remove(str(identified[id]))
                groups[i] = group
        i += 1
    

def main():
    findallfruits()
    findoccuring()
    for group in groups:
        if(len(group[0])==1):
            identified[group[1][0]] = group[0][0]
    group = purge()

main()

for group in groups:
    print(group)
print("-------------")
for id in identified:
    print(id + " : " + str(identified[id]))
