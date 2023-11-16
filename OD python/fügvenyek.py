# M

import math

# O

# F

pontok = []

def X(szog, r):
    return(math.cos(szog)*r)

def Y(szog, r):
    return(math.sin(szog)*r)

def radian(alfa):
    return(alfa * math.pi / 180)

def feltolt():
    r = 100
    for i in range(0,359):
        p = {}
        p["alfa"] = i
        p["r"] = r
        p["x"] = X(radian(i),r)
        p["y"] = Y(radian(i),r)
        pontok.append(p)



def kiir():
    for i in range(0,len(pontok)):
        print(f"{pontok[i]['alfa']:7.2f} foknál X= {pontok[i]['x']:10.4F}; Y={pontok[i]['y']:10.4F}.")


# PT

# Pont {"x":...,"y": ..., "alfa":..., "r"...}

feltolt()

kiir()