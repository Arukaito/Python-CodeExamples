#Iniciamos las variables como objetos basicos
x = object()
y = object()

#Multiplicamos los objetos * 10 utilizando operadores basicos
x_list = ([x]*10)
y_list = ([y]*10)

#Concatenamos las listas anteriores para obtener el resultado de [x]*10 y [y]*10 concatenado para que su resultado sea 20
big_list = x_list + y_list 


#Imprimimos la informacion que contienen nuestras variables
print("x_list contiene %d objects" % len(x_list))
print("y_list contiene %d objects" % len(y_list))
print("big_list contiene %d objects" % len(big_list))

# Condicionales para ver si el programa esta correcto
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Casi....")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Perfecto")
