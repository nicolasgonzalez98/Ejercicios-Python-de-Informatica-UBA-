cons=int(input("Adivine el número del 1 al 10:"))

if cons!=8:
    print("No.")
    c=int(input("Intenta otra vez:"))


    if c!=8:
        print("No.")
        d=int(input("Ultima oportunidad: "))


        if d!=8:
            print("Perdiste, perdiste, no hay nadie peor que vos!")
        else:
            print("Acertaste!")
    else:
            print("Acertaste!")
else:
    print("Acertaste!")


