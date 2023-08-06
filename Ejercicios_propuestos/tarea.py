listafib = [1,1]

for n in range (0,100):
    listafib.append(listafib[len(listafib)-1] + listafib[len(listafib)-2])

print("listafib", listafib)

#.pop para remover

docto= open("fib.txt", "w") #w indica que es de escritura
for i in range(len(listafib)):
    print(listafib[i], file = docto)
docto.close()


#otra forma
lprueba = [1,1]

for r in range (100):
    lprueba.append(lprueba[r] + lprueba[r+1])
print(lprueba)

paises = ["China", "India", "Estados Unidos", "Indonesia"]
poblaciones = [1391, 1364, 327, 264]
x= list(zip(paises, poblaciones))
print(x)