import random as rn


num=rn.randint(1,10)

print(num)


dif=int(input("Ingrese la cantidad de intentos: "))
i=dif

while dif>3:
    dif=int(input("Ingrese la cantidad de intentos: "))
    i=dif

f=True

while f:
    if i==0:
        print("Perdiste")
        f=False
        exit()
    g=int(input("Adivine un numero del 1 al 10: "))
    if g==num:
        print("Ganaste!")
        f=False
    if g!=num:
        print("Intenta otra vez!")
    i=i-1        
    
