n1=int(input("Ingrese un numero positivo: "))
n2=int(input("Ingrese un segundo numero positivo: "))

if n1>0 and n2>0:
                                if n1>n2:
                                                                dif=int(n1-n2)
                                                                if dif>n2:
                                                                    print("La diferencia es:", dif, ",mayor que", n2)
                                                                elif dif<n2:
                                                                    print("La diferencia es:", dif,",la cual es menor a ", n2)
                                elif n2>n1:
                                    dif2=int(n2-n1)
                                    if dif2<n1:
                                        print("La diferencia es:", dif2,",la cual es menor a ", n1)
                                    elif dif2>n1:
                                        print("La diferencia es:", dif2, ",mayor que", n1)
else:
    print("Ingresaste un numero invalido.")
            

    
