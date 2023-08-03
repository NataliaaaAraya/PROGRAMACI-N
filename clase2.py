s = "brunoamigogei"
print(s[:5])
print(s[5:10])

s = "king arthur"
print(s[::2]); print(s[-1:3:-1])

a = "ternura69"
print(a.isalpha())

a = "aaa"
print(a.isalpha())

print(",".join(("one","two","three")))

print("\n".join(reversed(("one","two","three"))))

x= "uno dos tres cuatro"
x.split()

z= "uno y dos y tres y cuatro"
z.split("y")

heading = "|     tabla de la locura      |"
line = "+" + "-"*16 + "+" + "-"*13 + "+"
linex = "+" + "-"*29 + "+"
print(line, heading, line,
    "|  Nov 23 1897 |          100 |",
    "|  Nov 25 1234 |          235 |",
    "|  feb  1 1234 |         1234 |", linex,  sep= "\n")


print('{:11,d}'.format(1000000))
"{:11,.1f}".format(1000000.)

lista = []
lista.append(1)
lista.append(2)
lista.append(4)
lista.pop(0) #si pongo pop() me borra el ultimo q esta en la lista
print(lista)

listab = [5,8,7]

lista.extend(listab)
print(lista)

listaC = []

for n in range (1,4):
    listaC.append(n)
    print("listaC: ", listaC)


f= open("powers.txt", "w") #w indica que es de escritura
for i in range(1, 1001):
    print(i, i**2, i**3, i**4, sep="," , file=f)
f.close()



f= open("powers.txt", "r")
squares, cubes, fourts = [], [], []
for line in f.readlines():
    fields = line.split(",")
    squares.append(int(fields[1]))
    cubes.append(int(fields[2]))
    fourts.append(int(fields[3]))

f.close()
n=500
print(" ")
print(n, "es", cubes[n-1])


#importamos las librerias que necesitemos
import math

#definimos variables e ingresamos
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

discriminante = b**2 - 4*a*c

if discriminante > 0:
        # Dos raíces reales y diferentes
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        print('La ecuacion posee dos raíces reales y diferentes')
        print('La raiz 1: ', raiz1)
        print('La raiz 2: ', raiz2)
    
elif discriminante == 0:
        # Dos raíces reales e iguales
        raiz = -b / (2*a)
        print('La ecuacion posee dos raíces reales y diferentes')
        print('La raiz es: ', raiz)
else:
        # Raíces complejas
        print("La ecuacion posee raíces complejas")