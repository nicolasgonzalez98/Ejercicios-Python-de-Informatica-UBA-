contactos=[]

nom=input("Ingrese el nombre del contacto(* para salir): ")

while nom!='*':
    apel=input("Ingrese el apellido de %s:" %nom)
    wp=input("Ingrese el numero de %s:" %(nom+" "+apel))
    contactos.append((nom,apel,wp))
    nom=input("Ingrese el nombre del contacto(* para salir): ")
print()
print("Agenda")
print()

for i in range(len(contactos)):
    print(contactos[i][0][:10].rjust(12,"/"),contactos[i][1][:10].ljust(12),contactos[i][2][:13].ljust(15),end="")
    num1=str(contactos[i][2])
    n=list(num1)
    if n[0]=='5' and n[1]=='4':
        print("Numero argentino")
    else:
        print("Numero extranjero")
    
    
    
