# Operaciones Aritméticas
# Suma
print("Ingrese el primer valor:")
a = int(input())
print("Ingrese el segundo valor:")
b = int(input())
suma = a + b
print("La suma es:", suma)

# Resta
print("Ingrese el primer valor de la resta:")
a = int(input())
print("Ingrese el segundo valor de la resta:")
b = int(input())
resta = a - b
print("La resta es:", resta)

# Multiplicación
print("Ingrese el primer valor de la multiplicación:")
a = int(input())
print("Ingrese el segundo valor de la multiplicación:")
b = int(input())
multiplicacion = a * b
print("La multiplicación es:", multiplicacion)

# División
print("Ingrese el primer valor de la división:")
a = int(input())
print("Ingrese el segundo valor de la división:")
b = int(input())


if b == 0:
    print("La division no se puede realizar")
else:    
    division = a / b
    print("La división es:", division)
