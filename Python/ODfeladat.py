import random

lista = []
for szám in range(10):
    vélszám=random.randint(1000,2000)
    lista.append(vélszám)
print(lista)


#a lista elemeinek összege
összeg = 0
for szám in lista:
    összeg += szám
print(f" A lista elemeinek összege {összeg}")

darab = 0 
for szám in lista:
    if szám %3 == 0:
        darab += 1
print(f" a listában { darab} db 3-mal osztható szám van")


#átlag
átlag = összeg / len (lista)
print(f"A lista átlaga: {átlag}")