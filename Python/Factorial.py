#Factorial de un numero

import os
os.system('cls'if os.name == 'nt' else 'clear') 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Ingresa un numero: "))
print("El factorial de ",num," es: ",factorial(num))