import numpy as np 
import random

Num= [random.randint(1,10) for _ in range(101)]
print(Num)

diccionario = {}

frecuencia = []

for i in range(1,11):
    Contar=0
    for x in Num:
       if i == x: 
            Contar+=1
    print("número "+ str(i) + ": " + str(Contar) + "veces")
    #frecuencia.append(Contar)
    diccionario [i] = Contar

print(diccionario)
#print(frecuencia)

mayor= max(diccionario.values())
indice_mayor= [a for a in range(1,11) if diccionario[a]== max(diccionario.values())]

menor= min(diccionario.values())
indice_menor= [a for a in range(1,11) if diccionario[a]== min(diccionario.values())]

print("numero que mas se repite " + str(indice_mayor) + " con un recuento de " + str(mayor) + " oportunidades")
print("numero que menos se repite" + str(indice_menor) + "con un recuento de " + str(menor) + " oportunidades")


#mayores= max(str(Contar))
#print(mayores)

    #print("numeros que mas se repiten: " + str(i) + "con un recuento de " + np.max(str(Contar)) + "oportunidades")
