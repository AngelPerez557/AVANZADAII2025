import os
os.system('cls'if os.name == 'nt' else 'clear')

print("Ingrese la tabla que desea ver")
num = int(input())


for i in range(1,11):
    print(num, "x", i, "=", num*i)

