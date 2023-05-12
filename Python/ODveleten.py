import random 


lista = []
for szám in range(6):
    vélszám=random.randint(50,100)
    lista.append(vélszám)
print(lista)




darab = 0
for szám in lista:
    if szám % 2 == 0: 
        darab +=1
print(f"A listában { darab} db páros szám található")


darab = 0
for szám in lista:
    if szám % 2 > 0: 
        darab +=1
print(f"A listában { darab} db páratlan  szám található")
