recetas=[]

ingrediente=input("Ingrese el ingrediente (escriba * para salir): ")

while ingrediente!="*":
    cant=float(input("Ingrese la cantidad de %s: "%ingrediente))
    uni=int(input("Ingrese unidad:\n1-gr\n2-ml\n3-cm3\n4-taza\n5-cuch.\n6-cuchdita"))
    while uni>6 or uni<1:
        uni=int(input("Ingrese unidad:\n1-gr\n2-ml\n3-cm3\n4-taza\n5-cuch.\n6-cuchdita\nInserte numero: "))
    recetas.append((ingrediente,cant,uni))
    ingrediente=input("Ingrese el ingrediente (escriba * para salir): ")


for i in range(len(recetas)):
    print(recetas[i][0],recetas[i][1],end="")
    unidad=str(recetas[i][2])
    if unidad=="1":
        print(" gr")
    elif unidad=="2":
        print(" ml")
    elif unidad=="3":
        print(" cm3")
    elif unidad=="4":
        print(" tazas")
    elif unidad=="5":
        print(" cuch.")
    elif unidad=="6":
        print(" cuchdita.")
        
