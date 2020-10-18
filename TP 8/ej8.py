def carga(lista):
    num=int(input("Ingresar numeros entre 1 y 1000 (pulse 0 para salir) : "))
    while num!=0:
        if num>0 and num<1001:
            lista.append(num)
        else:
            print("Numero erroneo")
        num=int(input("Ingresar numeros entre 1 y 1000 (pulse 0 para salir) : "))

def valor(lista):
    res=[]
    for i in range(len(lista)):
        if lista[i]%10==0:
            res.append(lista[i])
    return res
            




lista=[]
carga(lista)
resultado=valor(lista)
print(resultado)


    
