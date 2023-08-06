import numpy as np 
import matplotlib.pyplot as plt 
import random


Num= [random.randint(1,10) for _ in range(101)]

frecuencia = {
    numero: 0 for numero in range(1, 11)
}

for x in Num:
    if x in frecuencia:
        frecuencia[x] += 1
    else:
        frecuencia[x] = 1

mayor = max(frecuencia.values())

indice_mayor = [a for a in frecuencia.keys() if frecuencia[a] == mayor]

print(frecuencia)

menor= min(frecuencia.values())
indice_menor= [a for a in range(1,11) if frecuencia[a]== menor]

print("numero que mas se repite " + str(indice_mayor) + " con un recuento de " + str(mayor) + " oportunidades")
print("numero que menos se repite" + str(indice_menor) + "con un recuento de " + str(menor) + " oportunidades")

plt.bar(frecuencia.keys(), frecuencia.values())
plt.show()

plt.boxplot(frecuencia)
plt.show()

plt.violinplot(Num)
plt.show()