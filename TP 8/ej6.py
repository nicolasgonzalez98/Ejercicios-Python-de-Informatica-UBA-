def carga(lista):
    apel=input("Ingrese apellido (pulse * para salir): ")
    while apel!='*':
        nom=input("Ingrese nombre: ")
        tel=int(input("Ingrese telefono: "))
        mov=int(input("Ingrese el movil: "))
        lista. append([apel,nom,tel,mov])
        apel=input("Ingrese apellido (pulse * para salir): ")

agenda=[]
carga(agenda)
print(agenda)
agenda.sort(key=lambda agenda:(agenda[1].capitalize(),agenda[0].capitalize()))
for n in agenda:
    print(n)
            
