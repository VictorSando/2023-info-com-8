#Crea un programa que pida al usuario el radio de un círculo y muestre su
#diámetro (r.2), su circunferencia(2*pi*r) y su área(pi*r**2).
#Supón que pi es aproximadamente 3.14159.
pi=3.14159
radio=float(input('escriba el radio del circulo:'))
print(f'el diametro del círculo diametro es: {radio*2}')
print(f'la circunferencia del circulo es:{2*pi*radio}')
print(f'el area del circulo es:{pi*radio**2}')