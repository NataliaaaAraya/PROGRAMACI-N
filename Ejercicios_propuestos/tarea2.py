import numpy as np

materia= str(input("ingrese la materia (FIN SI NO HAY MAS):"))
materias= []

while materia.upper() != "FIN":
    materias.append(materia)
    materia= str(input("ingrese la materia (FIN SI NO HAY MAS):"))
print(materias)
#ctrl c

porcentajes= []

for i in range(len(materias)):
    porcentaje= int(input("ingresa el porcentaje"))
    porcentajes.append(porcentaje)
print(porcentajes)

alumno= str(input("ingrese el alumno (FIN SI NO HAY MAS):")).upper()
alumnos= []

while alumno != "FIN":
    alumnos.append(alumno)
    alumno= str(input("ingrese el alumno (FIN SI NO HAY MAS):"))
print(alumnos)

Matrnotas = np.zeros([len(materias), len(alumnos)])

for fila in range(len(materias)):
    print("Ingrese notas para "+ materias[fila] )
    for columna in range(len(alumnos)):
        nota= float(input("ingrese nota para " + alumnos[columna] + ": "))
        Matrnotas[fila][columna] = nota

print(Matrnotas)

#MATERIA DE CLASE 3 AHI ESTA COMO ENCONTRAR EN SUBLISTA

mejores_notas = []
mejores_alumnos = []

for fila in range(len(materias)):
    mejor_nota = np.max(Matrnotas[fila])
    indice_mejor_nota = np.argmax(Matrnotas[fila])
    mejor_alumno = alumnos[indice_mejor_nota]
    mejores_notas.append(mejor_nota)
    mejores_alumnos.append(mejor_alumno)

    print(indice_mejor_nota)


print("Mejores notas por materia:")
for i in range(len(materias)):
    print("la mejor nota en la evaluación de " + materias[i] + " fue: ") 
    print("nota: " + str(mejores_notas[i]) + "    Alumno: " + mejores_alumnos[i])

            #str
menorNota = 1000  # Inicializar con un valor infinito
nombrepeor = ""

for fila in range(len(materias)):
    menor_nota = np.min(Matrnotas[fila])
    if menor_nota < menorNota:
        menorNota = menor_nota
        indice_menor = np.argmin(Matrnotas[fila])
        nombrepeor = alumnos[indice_menor]

print("peor nota de curso:")
print(nombrepeor + " obtuvo un: " + str(menorNota))

promedios_ponderados = []

for columna in range(len(alumnos)):
    promedio_alumno = 0
    for fila in range(len(materias)):
        promedio_alumno += Matrnotas[fila][columna] * (int(porcentajes[fila]) / 100)
    promedios_ponderados.append(promedio_alumno)

# Encontrar el alumno con el menor promedio ponderado
indice_peor_promedio = np.argmin(promedios_ponderados)
peor_promedio = promedios_ponderados[indice_peor_promedio]
nombre_peor_promedio = alumnos[indice_peor_promedio]

print("peor promedio ponderado")
print(nombre_peor_promedio + " obtuvo un:  "+ str(peor_promedio))

mejores_notas = []
materias_mejores_notas = []
alums_mejors_notas= []

for fila in range(len(materias)):
    mejor_nota = np.max(Matrnotas[fila])
    mejores_notas.append(mejor_nota)
    indice_mejor = np.argmax(Matrnotas[fila])
    mejor_alumno = alumnos[indice_mejor]
    materias_mejores_notas.append(materias[fila])
    alums_mejors_notas.append(mejor_alumno)

# Encontrar la materia con la mejor nota
mejor_nota_global = np.max(mejores_notas)
indice_materia_mejor = np.argmax(mejores_notas)
materia_mejor_nota = materias_mejores_notas[indice_materia_mejor]
alumno_mejor = alums_mejors_notas[indice_materia_mejor]

print("mejores notas del curso")
print("alumno "+ alumno_mejor + " obtuvo un: " + str(mejor_nota_global) + "en la prueba " + materia_mejor_nota )


print(indice_materia_mejor)