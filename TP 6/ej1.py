menu=[]
dias='Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado'
dificultad=('',"Baja","Media","Alta")
uni=('','vaso', 'cuch', 'cuchdta', 'unid', 'gr', 'cm3', 'ml')

for dia in dias:
    plato=input("Ingrese el nombre del plato del dia %s: "%dia)
    dif=int(input("Ingrese dificultad\n1-Baja\n2-Media\n3-Dificil\n"))
    while dif not in (1,2,3):
        dif=int(input("Ingrese dificultad\n1-Baja\n2-Media\n3-Dificil\n"))       
    tiempo=int(input("Ingrese tiempo en minutos: "))
    ingredientes=[]
    ing=input("Ingrese los ingredientes del plato (pulse * para salir): ")
    while ing!="*":
        cant=int(input("Ingrese cantidad: "))
        print("Medidas")
        for i in range(1,len(uni)):
            print(i,"-",uni[i])
        unidad=int(input("Elija una: "))
        while unidad not in (1,2,3,4,5,6,7):
                unidad=int(input("Elija una: "))
        ingredientes.append((ing,cant,uni[unidad]))
        ing=input("Ingrediente (pulse * para salir): ")
    menu.append([plato,dificultad[dif],tiempo,ingredientes])

n=True

while n:
    print("Elija el dia de la semana(Pulse * para salir): ")
    for i in range(0,len(dias)):
        print(i,'-',dias[i])
    d=int(input())
    if d=='*':
        n=False
    else:
        print("El plato del dia es: ")
        print(menu[d][0])
        print("Dificultad: ",menu[d][1])
        print("Lleva aprox. %s minutos"%(menu[d][2]))
        print("Sus ingredientes son: ")
        for i in range(1,len(ingredientes[d])):
            print(menu[d][3][i], end="")
                       
