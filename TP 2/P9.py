n1=int(input("Ingrese la primer nota: "))
n2=int(input("Ingrese la segunda nota: "))
n3=int(input("Ingrese la tercer nota: "))
prom=(n1+n2+n3)/3





if n1>=4 and n2>=4 and n3>=4 and round(prom,)>7:
    print("Promiedio final:",round(prom,))
    print("Promocionaste")
elif n1>=4 and n2>=4 and n3>=4 and round(prom,)<=7:
    print("Promiedio final:",round(prom,))
    print("El alumno debera rendir final")
else:
    rec=int(input("Ingrese la nota del recuperatorio: "))
    fin=(n1+n2+n3+rec)/4
    print("Promiedio final:",round(fin,))
    if rec>=4:
        print("El alumno deberá rendir final.")
    else:
        print("El alumno no es regular.")
    
    


