# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:42:29 2021

@author: Licht
"""

# De los n elementos de un vector dado calcule:
# a. La sumatoria
# b. La productoria
# c. El Mayor Elemento
# d. El menor Elemento

l1 = [1, 2, 3, 4, 5, 6]
i = 0
sum = 0
prod = 1
for n in l1:
    sum += n
print(f'El resultado de la sumatoria es: {sum}')
while i < len(l1):
    prod = prod * l1[i]
    i += 1
print(f'El resultado de la prudcotria es: {prod}')

print('El número máximo es: ')
print(max([int(num) for num in l1]))
print('El número mínimo es: ')
print(min([int(num) for num in l1]))


# De los n elementos de un vector dado calcule:
# a. Cantidad de elementos pares
# b. Cantidad de elementos impares
# c. Cantidad de elementos primos

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
cont1 = 0
cont2 = 0
cont_primos = 0
es_primo = 0
for i in lista:
    if i % 2 == 0:
        cont1 += 1
    if i % 2 != 0:
        cont2 += 1
    if(isPrime(i)):
        cont_primos += 1
print(f'La cantidad de elementos pares es de: {cont1}')
print(f'La cantidad de elementos impares es de: {cont2}')
print("la cantidad de numeros primos es: {}".format(cont_primos))


# Dado un Vector v y un Vector v1 de cómo resultado un Vector resultante de
# las siguientes operaciones:
# a. Suma
# b. Resta

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
l3 = []
l4 = []
for i in range(len(l1)):
    l3.append(l1[i] + l2[i])
print(f'La suma de los vectores es: {l3}')

for i in range(len(l1)):
    l4.append(l1[i] - l2[i])
print(f'La resta de los vectores es: {l4}')

# De los n elementos de un vector dado identifique el número que mas se
# repite e indique cual es.


# Dado dos vectores númericos A y B debe realizar las siguiente operaciones
# con conjuntos:
# a. Unión: Conjunto que contiene(sin repetir) los elementos de A y B.
# b. Intersección: Conjunto que contiene los elementos comunes que
# aparecen en los conjuntos A y B
# c. Diferencia(A-B) Conjunto formado por los elementos que pertenecen
# al conjunto A y no pertenecen al conjunto B.
# d. Diferencia (B-A) Conjunto formado por los elementos que pertenecen
# al conjunto B y no pertenecel al conjunto A.

l1 = [1, 2, 3, 4]
l2 = [1, 5, 6, 4, 7]
s1 = set(l1)
s2 = set(l2)
s3 = s1 & s2
l3 = list(s3)
l1.extend([element for element in l2 if element not in l1])
l4 = list(set(l1) - set(l2))
print(f'Unión: {l1}')
print(f'Intersección: {l3}')
print(f'Diferencia A-B: {l4}')




























