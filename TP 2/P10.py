num=int(input("Ingrese un numero positivo: "))

if num>0:
    if num==1:
        print("1 es el primer impar")
    elif (num%2)==0:
        print("Siguiente par es:", num+2)
    elif (num%2)!=0:
        print("Anterior impar es:", num-2)
else:
    print("Ingresa un numero positivo")
