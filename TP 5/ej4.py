lista=[]

nico=True

while nico:
    num=int(input("Ingrese un numero entero positivo: "))
    if num==0:
        print("Muchas gracias!")
        nico=False
    if num not in lista:
        if num>0:
            lista.append(num)
    else:
        print("Ese numero ya lo introduciste")

print("Hay", len(lista), "numeros cargados")

    


print("Lista resultante")
print(lista)
