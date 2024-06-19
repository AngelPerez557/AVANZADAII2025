#imprime 10 valores con el ciclo while

i = 0

while i < 10:
    print(i)
    i += 1

print("ciclo terminado por banderin")
while True:
    entrada = input("ingrese s para salir")
    if entrada == "s":
        break
    print("ciclo controlado por banderin 2")
    bandera = "x"

    while bandera != "s":
        bandera = input("ingrese s para salir")