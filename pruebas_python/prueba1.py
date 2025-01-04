mensaje = "esto es una prueba"
print(mensaje[5:10])
print(len(mensaje))
print(mensaje.find('prueba')) # función para encontrar
print(mensaje.upper()) # función para mayuscula
print(mensaje.lower()) # función para minuscula
cambio=mensaje.replace("prueba", "pruebalo") # función para reemplazar
print(cambio)
print(type(mensaje))

lista = [3,'hola', True, 'prueba']
print(len(lista))

print(mensaje.index("esto")) # buscar posición
poner = lista.insert(1, "estas") # inserta un elemento en una lista
print(lista)

ponerfinal = lista.append("cosa") # inserta elemento al final
print(lista)

remover = lista.remove('hola') # eliminar
print(lista)


# TUPLAS - elementos separado por comas - inmutables
tupla = "hola", 3.4, True, 'Hola'
tupla
 
w,x,y,z = tupla
print(x)
print(tupla[1])

#Diccionarios - estructura de datos - pares de (clave,valor)

diccionario = {
        'clave1': 'primer valor',
        'clave3': 'mi tercer valor',
        'clave2': 'segundo valor'
}

print(diccionario['clave2'])

diccionario['clave3'] = 'prueba'
print(diccionario['clave3'])

del diccionario['clave2']

print(list(diccionario)) # lista las claves del diccionario # sorted (lista ordenada)

# comprobar si una clave se encuentra en el diccionario

'clave1' in diccionario


# sentencia if condicional - ejecuta un bloque de instrucciones si devuelve true
print("Escribe un numero de 1 a 10")
number = int(input())
if (number > 5):
    print("!Soy mayor que 5¡")

    


