nom1=input("Ingrese el nombre de una persona: ")
eda1=int(input("Ingrese la edad: "))
nom2=input("Ingrese el nombre de la segunda persona: ")
eda2=int(input("Ingrese la edad de la segunda persona: "))
nom3=input("Ingrese el nombre de la tercera persona: ")
eda3=int(input("Ingrese la edad de la tercera persona: "))

if eda1<eda2 and eda1<eda3:
    print("El más joven es", nom1,"con", eda1,"años")
elif eda2<eda1 and eda2<eda3:
    print("El más joven es", nom2,"con", eda2,"años")
else:
    print("El más joven es", nom3,"con", eda3,"años")

if eda1>eda2 and eda1>eda3:
    print("El más viejo es", nom1,"con", eda1,"años")
elif eda2>eda1 and eda2>eda3:
    print("El más viejo es", nom2,"con", eda2,"años")
else:
    print("El más viejo es", nom3,"con", eda3,"años")






