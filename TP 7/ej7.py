def elim_cadenas(a):
    a=a.split(" ")
    b=list(a)
    print(b)
    cad=input("Ingrese una cadena a eliminar: ")
    for i in range(len(b)-1):
        if b[i]==cad:
            b.pop(i)
    for i in range(len(b)):
        if b[i]==cad:
            b.pop(i)
    b=" ".join(b)
    return b



texto="Danilo se fue a Paris"

print(elim_cadenas(texto))

