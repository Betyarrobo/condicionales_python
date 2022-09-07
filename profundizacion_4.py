# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

import string


print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio


# Ejemplos varialbles de texto y condicionales compuestos
print ("Digite las palabras")
p1 = input ("Digite la  palabra 1: ")
p2 = input ("Digite la  palabra 2: ")
p3 = input ("Digite la  palabra 3: ")

print ("Elija la opcion para ordenar las palabras ingresadas")
print ("1 - Ordenar por orden alfabetico 1 ")  
print ("2 - Ordenar por cantidad de letras 2")

op = int(input ("Ingrese la opcion deseada: "))

if op == 1:
    print ("ORDENAMIENTO DE MAYOR A MENOR")
    if p1 > p2 and p2 > p3:
        print ("El orden es palabra 1:{}, palabra2: {}, palabra3: {}".format(p1, p2, p3))
    elif p1 > p2 and p3 > p2 and p1 > p3:
        print ("El orden es palabra 1:{}, palabra3: {}, palabra2: {}".format(p1, p3, p2))
    elif p2 > p1 and p1 > p3:
        print ("El orden es palabra 2:{}, palabra1: {}, palabra3: {}".format(p2, p1, p3))
    elif p2 > p1 and p3 > p1 and p2 > p3:
        print ("El orden es palabra 2: {}, palabra3: {}, palabra1: {}".format (p2, p3, p1))
    elif p3 > p1 and p1 > p2:
        print ("El orden es palabra 3:{}, palabra1: {}, palabra2: {}".format(p3, p1, p2))
    elif p3 > p1 and p2 > p1 and p3 > p2:
        print ("El orden es palabra 3: {}, palabra2: {}, palabra1: {}".format (p3, p2, p1))
        
elif op == 2: 
    print ("ORDENAMIENTO SEGUN CANTIDAD DE CARACTERES DE MAYOR A MENOR")
    longuitud_p1 = len(p1)
    longuitud_p2 = len(p2)
    longuitud_p3 = len(p3)
    if longuitud_p1 > longuitud_p2 and longuitud_p2 > longuitud_p3:
        print ("El orden es palabra1: {}, caracteres: {}, palabra2: {}, caracteres: {}, palabra3: {}, caracteres: {}".format (p1, longuitud_p1, p2, longuitud_p2, p3, longuitud_p3))
    elif longuitud_p1 >longuitud_p2 and longuitud_p3 > longuitud_p2 and longuitud_p1 > longuitud_p3:
        print ("El orden es palabra1: {}, caracteres: {}, palabra3: {}, caracteres: {}, palabra2: {}, caracteres: {}".format(p1, longuitud_p1, p3, longuitud_p3, p2, longuitud_p2))
    elif longuitud_p2 > longuitud_p1 and p1 > p3:
        print ("El orden es palabra2: {}, caracteres: {}, palabra1: {}, caracteres: {}, palabra3: caracteres:{}".format(p2, longuitud_p2, p1, longuitud_p1, p3, longuitud_p3))
    elif longuitud_p2 > longuitud_p1 and longuitud_p3 > longuitud_p1 and longuitud_p2 > longuitud_p3:
        print ("El orden es palabra2: {}, caracteres: {}, palabra3: {}, caracteres: {}, palabra1: {}, caracteres: {}".format(p2, longuitud_p2, p3, longuitud_p3, p1, longuitud_p1))
    elif longuitud_p3 > longuitud_p1 and longuitud_p1 > longuitud_p2:
        print ("El orden es palabra3: {}, caracteres: {}, palabra1: {}, caracteres: {}, palabra2: {}, caracteres: {}".format(p3, longuitud_p3, p1, longuitud_p1, p2, longuitud_p2))       
    elif longuitud_p3 > longuitud_p1 and longuitud_p2 > longuitud_p1 and longuitud_p3 > longuitud_p2:
        print ("El orden es palabra3: {}, caracteres: {}, palabra2: {}, caracteres: {}, palabra1: {}, caracteres: {}".format(p3, longuitud_p3, p2, longuitud_p2, p1, longuitud_p1))
  


