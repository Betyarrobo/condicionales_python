# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición


# ejecicio resuelto
# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda
if numero_1 > numero_2:
    print('numero_1:', numero_1, 'Este numero es mayor a numero_2:',numero_2)
else:
    print('numero_2:', numero_2, 'Este numero es mayor a numero_1:',numero_1)

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso


if(numero_1 > 0):
    print('En numero {} es positivo!!' .format(numero_1))
elif(numero_1 <0):
    print('El numero {} es negativo!!' .format(numero_1))
else:
    print('El numero es CERO!!')

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición
 
if numero_1 >=0 and numero_1 <=100:
    print('numero_1:', numero_1, 'Este numero esta entre el rango de  mayor a 0 y menor a 100:',numero_1)
else:
    print('numero_2:', numero_2, 'Este numero esta fuera del  rango de  mayor a 0 y menor a 100:',numero_2)


# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición


if numero_1 <10 or numero_2 >=-2 :
     print('El numero ' ,numero_1, ' es menor que 10 O el numero ',numero_2, ' es mayor que -2')
else:
    print('El numero ' ,numero_1, ' NO es menor que 10 O el numero ',numero_2, ' NO es mayor que -2')
    print('Felicidades hemos finalizado este ejerccicio con exito')
