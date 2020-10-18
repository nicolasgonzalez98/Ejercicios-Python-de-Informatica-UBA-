import random

n=random.randint(0,30)

dif=int(input("Elija el nivel de intentos(10-15-20): "))


while dif!=10 and dif!=15 and dif!=20:
    dif=int(input("Elija el nivel de intentos(10-15-20): "))


i=dif

numeros=set()
f=True
g=0

while len(numeros)<i and f:
    num=int(input("Adivine un numero entre 0 y 30: "))
    g=g+1
    if num<0 or num>30:
        print("Ingresaste un numero equivocado")
    if num>=0 and num<=30:
        numeros.add(num)
        if num==n:
            print("Acertaste")
            f=False
    if g==i:
        print("Perdiste")
        


    
