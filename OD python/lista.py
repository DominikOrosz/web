


#Készítsünk egy 100 egész, véletlen számból álló listát, és irasuk ki!              

import random as rand 

# mátrix elkészítése 

szinek = []

for i in range (0,10):
     szinek.append([])
     for j in range(0,3):
          szinek[-1].append(rand.randint(0,255))

for i in range(0,10):
     print(f"rgb ({szinek[i][0]},{szinek[i][1]},{szinek[i][2]})" )  
     print(f"#{szinek[i][0]:02x}{szinek[i][1]:02x}{szinek[i][2]:02x}")    