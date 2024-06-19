import os
os.system('cls'if os.name == 'nt' else 'clear')

print("Ingrese cualquier tipo de texto, y lo analizaremos")
mensaje=input()
mensaje.lower()

print("Ingrese que letra desea saber cuantas veces se repite")
letra=input()
veces=mensaje.count(letra)

print("la letra "+str(letra)+" se repite: "+str(veces)+" veces")