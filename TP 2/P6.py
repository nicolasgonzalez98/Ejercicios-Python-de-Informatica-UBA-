a1=float(input("Ingrese la distancia recorrida por el auto 1: "))
a2=float(input("Ingrese la distancia recorrida por el auto 2: "))
a3=float(input("Ingrese la distancia recorrida por el auto 3: "))

if a1>a2 and a1>a3:
    if a2>a3:
        print("1\n2\n3")
    elif a3>a2:
        print("1\n3\n2")
elif a2>a1 and a2>a3:
    if a1>a3:
        print("2\n1\n3")
    elif a3>a1:
        print("2\n3\n1")
elif a3>a1 and a3>a2:
    if a1>a2:
        print("3\n1\n2")
    elif a2>a1:
        print("3\n2\n1")
else:
    print("No pusiste un numero, infeliz")
