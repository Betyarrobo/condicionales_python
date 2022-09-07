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
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''




print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
mayor=0.0
menor=0.0
promedio=0.0
t_1 = float(input('Ingrese la primera temperatura:\n'))

t_2 = float(input('Ingrese la segunda temperatura:\n'))

t_3 = float(input('Ingrese la tercera temperatura:\n'))

if (t_1 > t_2):
    mayor=t_1
    menor=t_2
else:
    mayor=t_2
    menor=t_1
    if (mayor < t_3):
        mayor=t_3
    if (menor > t_3):
        menor=t_3
prom=(t_1+t_2+t_3)/3
print("La maxima temperatura es:",mayor)
print("La minima temperatura es:",menor)
print("El promedio es:",prom)
