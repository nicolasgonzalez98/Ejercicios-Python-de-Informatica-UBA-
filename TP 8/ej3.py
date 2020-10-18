lugares=["Buenos Aires","Brasilia","Santiago de chile","Lima","Quito","medellin","caracas"]

for i in range(len(lugares)):
    lugares[i]=lugares[i].capitalize()
lugares.sort()

print(lugares)


llenado=True
while llenado:
    lugar=input("Ingrese una ubicacion (Ingrese * para salir): ")
    lugar=lugar.capitalize()
    if lugar=='*':
        llenado=False
    if lugar!='*':
        if lugar in lugares:
            print("Te equivocaste.")
        else:
            lugares.append(lugar)
    lugares.sort()
    print(lugares)
        
    
    
