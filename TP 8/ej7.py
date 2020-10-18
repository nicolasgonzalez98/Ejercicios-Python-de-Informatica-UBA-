import random as rn

def carga(lista):
    while len(lista)<30:
        num=rn.randint(1,100)
        if num not in lista:
            lista.append([num])

def prom(lista):
    suma=0
    for i in range(len(lista)):
        suma=suma+lista[i][0]
    prom=suma/len(lista)
    return prom

def dif(lista):
    for i in range(len(lista)):
        if lista[i][0]>=prom(lista):
            promedio=lista[i][0]-prom(lista)
        else:
            promedio=prom(lista)-lista[i][0]
        lista[i].append(promedio)
            
    


lista=[]
carga(lista)
num=prom(lista)
print("El promedio de la lista es:",num)
dif(lista)
lista.sort(key=lambda lista:(lista[1],lista[0]))
for i in range(len(lista)):
    print(lista[i][0],' ',lista[i][1])
