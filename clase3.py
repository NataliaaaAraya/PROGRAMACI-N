import re #exprecion regular
import numpy as np 

a= np.array([[1,2,3,], [4,5,6]])
print(a[1, 0], "\n") #fila uno columna 0

print(a[1][0],"\n")

print(a[:, 0:2])

print(a[(a % 2 == 0)])
print(a[(a % 2 == 0) and (a>2)])

a= np.array([[1,2,3,], [4,5,6]])
b= np.array([1,1,1], [2,2,2])

print(a+b,"\n")
print(a/b,"\n")
print(a**b,"\n")  


