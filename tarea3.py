
import numpy as np

crd=[]
coordenadas = []
archivo= open("UNI_CORR_500_01.txt","r")
print(crd)
print(coordenadas)

for i in archivo.readlines():
    separa = i[0:29]
    aux = separa.split()
    crd.append(aux)
archivo.close()

for r in range(5,len(crd)):
    lista2 = crd[r]
    a = []
    X = lista2[2]
    Y = lista2[3]
    Z = lista2[4]
    a.append(float(X))
    a.append(float(Y))
    a.append(float(Z))
    coordenadas.append(a)

    k= int(input("ingrese: "))
    print("las coordenadas son ", k , ":", coordenadas[k])