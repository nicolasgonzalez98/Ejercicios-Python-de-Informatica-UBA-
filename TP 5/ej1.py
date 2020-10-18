lista=[]

while len(lista)<10:
    num=int(input("Agregue un numero a la lista: "))
    lista.append(num)



total=0

for i in range(0,10):
    total=total+lista[i]

prom=total/10

        


    





print("El menor numero de la lista es: ", min(lista))
print("El mayor numero de la lista es: ", max(lista))
print("El promedio es: ", prom)



    
