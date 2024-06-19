
print("BIENVENIDOS A SUS PELOTAS\n")
pelota = 10
print("Ingrese cuantas pelotas desea comprar")
compra = int(input())
total=compra*pelota

if compra >= 1000:
    total = total - (total * 0.50)
elif compra >= 10:
    total = total - (total * 0.20)



print("Su total a pagar es: ", total)
