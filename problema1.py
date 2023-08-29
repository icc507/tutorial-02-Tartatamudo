#Problema 1  / 8 ptos x4 pruebas / 32 puntos
#Concatenación de listas o tuplas
#--------------------------------
#Confeccione un programa que lea 2 tuplas sean t1 y t2
#La salida debe ser una tupla en el orden t2 t1 t2
#---------------------------------
#Ejemplo de entrada:
#         20 90 hola
#		  mundo 44
#La salida debe ser
#         ('mundo', 44, 20, 90, 'hola', 'mundo', 44)
t = input().split()
m = input().split()

for i in range(len(t)):
    try:
        t[i] = int(t[i])
    except ValueError:
        continue

for i in range(len(m)):
    try:
        m[i] = int(m[i])
    except ValueError:
        continue

print(tuple(m) + tuple(t) + tuple(m))
