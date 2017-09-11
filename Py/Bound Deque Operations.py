
#importamos deque
from collections import deque

#Deque es la funcion estadistica para hacer una cola recursiva que se va restando segun se le agregen valores
q = deque(maxlen=3)

#donde maxlen es el tamanio
#q = 1,2,3
q.append(1)
q.append(2)
q.append(3)

#y se le pueden agregar valores al deque pero cuando se agrega un extra al maxlen este se reacomoda y deja el ultimo fuera de la fila
q.append(4)

#Imprimimos resultado
# q = 2,3,4
print(q)