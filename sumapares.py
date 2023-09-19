print("ingrese el numero inicial")
i= int(input())
print("ingrese el numero final")
f = int(input())
suma=0
print("**los numeros pares del rango**")
while i <= f:
    if i % 2 == 0:
        print(i)
        suma = suma+i
    i+=1
print("la suma de los numeros es:",suma)
