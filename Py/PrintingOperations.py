#Aqui tenemos algunos ejemplos de como imprimir Strings y sus caracteres de Escape

#Escape --- Que hace?.
#\\ Backslash (\)
#\' Single- quote (')
#\" Double- quote                (")
#\a ASCII bell (BEL)
#\b ASCII backspace (BS)
#\f ASCII formfeed (FF)
#\n ASCII linefeed (LF)
#\N{name} Character named name in the Unicode database (Unicode only)
#\r ASCII carriage return (CR)
#\t ASCII horizontal tab (TAB)
#\uxxxx Character with 16- bit hex value xxxx (Unicode only)
#\Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
#\v ASCII vertical tab (VTm
#\ooo Character with octal value oo
#\xhh Character with hex value hh

Dias = "Lunes Martes Miercoles Jueves Viernes Sabado Domingo\n"

#utilizamos \n para hacer un salto de linea
Meses = "\nEnero\nFebrero\nMarzo\nAbril\nMayo\nJunio\nJulio\nAgosto\nSeptiembre\nOctubre\nNoviembre\nDiciembre\n"

#Imprimimos la secuencia de texto con la variable dias
print("Imprimimos mi variable de Dias: ",Dias)

#Imprimimos la variable de meses
print("Imprimimos la varia ble de meses: \n",Meses)

# Imprimimos una cadena de texto que no necesita formato
print("""Esta es una cadea de texto.
que se formatea de forma en la que tu la escribes.""")

# Caracteres de Escape de secuencia

gato_azul = "\t I'm Tabbed."
gato_rojo = "I'm split\non a line."
gato_verde = "I'm \\ a \\ cat"
gato_rosa = """I'm the best cat:
\t* I Have Food
\t* I Have Water
\t* I Have Catnip\n
"""

print (gato_azul)
print (gato_rojo)
print (gato_verde)
print (gato_rosa)

#Ejercicios 
#1 Usar ''' triple Single Quote y para que lo usariamos
#2 Combina secuencias de escape y y formatos para hacer un string mas complejo
#3 Utilizar %r (raw)