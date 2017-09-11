#importamos deque de la coleccion
from collections import deque

#asignamos deque para la variable Q sin limites(unbound)
q = deque()

#asignamos valores para la demostracion ya que no tiene limites se le pueden ir agregando valores

q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.appendleft(5)

#podemos utilizar las funciones pop() y popleft() para sacar valores que necesitamos


print("Donde el valor 4 es el caracter de la derecha \n del pop() en el deque  [5,1,2,3,*4*]")
print(q.pop())

print("Donde el valor 5 es el caracter de la izquierda \n del popleft() en el deque  [*5*,1,2,3,4]")
print(q.popleft())