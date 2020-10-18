l1=[]
for i in range(20):
    art=input("Ingrese el nombre del articulo N°%s: "%(i+1))
    l1.append([])
    l1[i].append(art)
    cant=1
    while cant>0:
        cant=int(input("Ingrese la cantidad de productos vendidos (Pulse 0 para salir): "))
        if cant>0:
            l1[i].append(cant)

print()

print("Articulos".center(9),"  ","Total Vendidos".center(16))

for i in range(len(l1)):
    print(l1[i][0].ljust(12), end=" ")
    suma=0
    for j in range(1,len(l1[i])):
        suma=suma+l1[i][j]
    print(str(suma).rjust(15))
    
    

        
    
    
