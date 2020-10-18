personas=[]

nom=input("Ingrese el nombre(Pulse * para salir): ")

while nom!="*":
    apel=input("Ingrese el apellido: ")
    apellido=apel.capitalize()
    nombre=nom.capitalize()
    personas.append((nombre,apellido))
    nom=input("Ingrese el nombre(Pulse * para salir): ")






for i in range(len(personas)):
    dim=len(personas[i][1])+1
    print(personas[i][1].ljust(dim, ","),personas[i][0][0])
