lista=[]

while len(lista)<10:
    num=int(input("Inserte un numero entero: "))
    lista.append(num)

print(lista)

lista.reverse()

print("Orden invertido: ")
print(lista)
