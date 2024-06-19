#ciclo for
import os
os.system('cls'if os.name == 'nt' else 'clear')

# for i in range(10):
#     print(i+1)

# lista = {"uno","dos","tres","cuatro","cinco"}
# for item in lista:
#     print(item)

# mi_tupla=(1,"dos",[3.33,"cuatro","equis"],(5.0,6))

# for item in mi_tupla:
#     print(item)

diccionario = {
    "Curso":"Python TOTAL",
    "Clase":"Ciclos",
    "Tema":"for",
    "Duracion":"1 Trimestre",
    "Profesor":"Angel Perez"
}

# for llave in diccionario:
#     print(llave, ": ",diccionario[llave])

    #invertir el orden de un diccionario

for llave in reversed(diccionario):
    print(llave, ": ",diccionario[llave])
