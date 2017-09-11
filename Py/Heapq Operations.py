#Problema: Si tu quieres hacer una lista de los objetos ( N ) de los mas grandes a los mas pequeños

#Solucion: El modulo Heapq tiene dos funciones - nlargest() y nsmallest() estas hacen exactamente lo que necesitamos 

#Importamos heapq

import heapq

#Creamos una lista numerica de numeros

listanumerica = [1,4,3,84,26,-5,18,25,37]

#utilizamos nlargest() y nsmallest() de heapq para demostrar sus funciones

print("Imprimimos heapq con los valores iniciales. para ver su resultado con los pr")
print(heapq.nlargest(1 ,listanumerica)) #Donde 1 es la cantidad de caracteres que queremos regresar
print(heapq.nsmallest(3,listanumerica))


#las funciones tienen un parametro Key='' que permite hacer analisis mas extensivos con datos mas grandes

portfolio = [
{'name': 'Alkaworks', 'shares': 100, 'price': 91.1},
{'name': 'AlkaMedia', 'shares': 50, 'price': 543.22},
{'name': 'Alka3D', 'shares': 200, 'price': 21.09},
{'name': 'AlkaSup', 'shares': 35, 'price': 31.75},
{'name': 'Alkanet', 'shares': 45, 'price': 16.35},
]


print("Utilizamos el Heapq con el parametro de tipo lamba para la columna price ")

baratos = heapq.nsmallest(1,portfolio,key=lambda s: s['price'])

print(baratos)

caros = heapq.nlargest(1,portfolio,key=lambda s: s['price'])


print(caros)
