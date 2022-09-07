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

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

n_1 = int(input('Ingrese el primer número:\n'))

n_2 = int(input('Ingrese el segundo número:\n'))


n_3 = int(input('Ingrese el tercer número:\n'))

if (n_1 % 2) == 0:
    print('Es par')
else:
    print('Es impar')
    
if (n_2 % 2) == 0:
    print('Es par')
else:
    print('Es impar')

if (n_3 % 2) == 0:
    print('Es par')
else:
    print('Es impar')