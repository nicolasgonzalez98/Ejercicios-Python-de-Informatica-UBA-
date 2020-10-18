num=int(input("Ingrese un numero de 3 cifras: "))
digito1=int(num//100)

digito3=int(num%10)

if num>=100 and num<1000:
    if digito1==digito3:
        print("Son capicuas")
    else:
        print("No son capicuas")
    
else:
    print("No es un numero de 3 cifras")
