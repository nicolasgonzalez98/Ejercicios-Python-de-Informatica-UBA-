valor=int(input("Valor de la compra: "))

if valor>500:
    imp=int(valor/4)
    print("Impuesto: ", round(imp,0))
else:
    imp=int(valor/3)
    print("Impuesto: ", round(imp,0))
    
