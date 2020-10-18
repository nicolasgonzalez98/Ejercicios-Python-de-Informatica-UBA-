aa=int(input("Ingrese un numero entero positivo: "))
be=int(input("Ingrese otro numero entero positivo: "))

if aa>0 and be>0:
    if aa>be:
        if aa%be==0:
            print(be,"es el MCD")
    else:
        fe=aa%be
        mcd=True
        while mcd:
            r=be%fe
            if r==0:
                print("%s es el MCD")
                mcd=False
            else:
                r=fe

        print("no tiene MCD")
            
    
else:
    print("Sos un violado.")

