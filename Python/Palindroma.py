import os
os.system('cls'if os.name == 'nt' else 'clear')

print("Ingrese una palabra para ver si es palindroma")
palabra = input()

palabra = palabra.lower()        
palabra_invertida = palabra[::-1] 

if palabra_invertida == palabra : 
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")    

