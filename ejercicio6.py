# Crea un programa que pida al usuario el radio de un círculo y calcule su área.
# La fórmula A = pi * r^2. Luego, muestra en pantalla el resultado.
# Supongamos que pi = 3.1416

pi=3.1416
radio=float (input('ingrese el radio : '))
print(f'el area del circulo es: {round (pi*radio**2,2)}')