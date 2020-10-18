n=1
while n<6:
    num=int(input("Ingrese un numero par: "))
    if num%2==0:
        if num%4==0:
            print("%s es un numero multiplo de 4"%num)  
        else:
            print("%s no es un numero multiplo de 4"%num)  
        n=n+1
    else:
        print("Ingresaste un numero impar")
