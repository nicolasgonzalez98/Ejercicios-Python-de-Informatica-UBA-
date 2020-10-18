num=int(input("Ingrese un numero: "))
div=int(input("Ingrese un divisor: "))

res=int(num%div)

if res==0:
    print(num, "es divisible por", div)
else:
    print(num, "no es divisible por", div)

    
