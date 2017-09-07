#Declaramos las variables de tipo lista vacias
numbers = []
strings = []

#Podemos declarar la variables de tipo lista con contenido ya incluido en Runtime
names = ["John","Eric","Jessica"]

#Podemos mandar a llamar la variable con el Indice apartir de 0 utilizando [] para acceder a los objetos de una lista
second_name = names[1]                                                                        

#Agregamos los numeros a la lista de numeros con la funcion Append que agrega objetos a la lista
numbers.append(1)
numbers.append(2)
numbers.append(3)

#Agregamos los strings a la lista de los strings utilizando append
strings.append("Hello")
strings.append("World")

#Utilizamos la lista junto con su indice para imprimir lo que queremos
print(numbers[1])
print(strings[0])
print("The Second Name On The Names List Is %s" % second_name)