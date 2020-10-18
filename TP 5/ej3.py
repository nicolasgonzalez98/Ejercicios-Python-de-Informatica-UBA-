lista=[]

f=True

while f:
    i=int(input("Ingrese un numero a graficar (si es negativo cerrara el programa): "))
    if i<0:
        f=False
    if i>=0:
        lista.append(i)

for i in range(0,len(lista)):
    print("*"*lista[i],"(", lista[i], ")")

