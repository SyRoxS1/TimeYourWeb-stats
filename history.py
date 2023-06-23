import os

nbW = 0 
time = 0
count = 0
error = 0
nbvir = 0
liste = os.listdir()
fichier = []
print(list)
site = str(input("Site ? : "))

for i in range(len(liste)):
    if "Summary - " in liste[i]:
        fichier.append(liste[i]) 
        print(fichier[count])
        count += 1
    
    
for z in range(count):
    f = open(fichier[z],"r",encoding="utf8")
    read = f.readlines()
    read = read[2:]
    f.close()

    for i in range(len(read)):
        y = 0
        while nbW!=2:
            if read[i][y] == '"':
                nbW += 1
            if read[i][y] == ',':
                nbvir += 1 
            y+= 1

        check = read[i].split(",")
        if site in check[0]:
            time = time + int(check[2+nbvir])
        nbW = 0
        nbvir = 0
        

            
        
time = time/60/60
print("temps en heures sur ",site,"en",count,"mois :",time)
print(error)