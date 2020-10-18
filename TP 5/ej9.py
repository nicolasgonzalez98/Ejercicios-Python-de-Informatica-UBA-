nombre=[]
apellidos=[]
wp=[]
nom=input("Ingrese el nombre del contacto, * para salir: ")
while nom!="*":
    apel=input('Ingrese el apellido de %s: ' %nom)
    num=int(input("Ingrese el numero de %s: " %(nom+' '+apel)))
    nombre.append(nom)
    apellidos.append(apel)
    wp.append(num)
    nom=input("Ingrese el nombre del contacto, * para salir: ")
print("Agenda")
for i in range(len(nombre)):
    print(nombre[i][:10].rjust(12,"/"),apellidos[i][:10].ljust(12),wp[i],end="")
    num1=str(wp[i])
    contacto=list(num1)
    if contacto[0]=='5' and contacto[1]=='4':
        print("Argentina".rjust(12))
    else:
        print("Extranjero".rjust(12))






    
    
