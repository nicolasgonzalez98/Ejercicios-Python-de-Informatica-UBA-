num=int(input("Ingrese un numero entero: "))

if num>0:
    im=int(input("Ingresar un numero impar: "))
    if im%2!=0:
        print("Es correcto")
    else:
        print("Es incorrecto")
elif num<0:
    par=int(input("Ingrese un numero par: "))
    if par%2==0:
        print("Es correcto!")
    else:
        print("Es incorrecto!")
else:
    print("Correcto!")
