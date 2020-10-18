 apl=0
apr=0
prom=0
i=True
n=0

while i:
    nota=int(input("Ingrese nota (para cerrar el programa aprete 8898): "))
    if nota<=10 and nota>=0:
        if nota<4:
            apl=apl+1
        elif nota<=7 and nota>=4:
            apr=apr+1
        elif nota<=10:
            prom=prom+1
        n=n+1
    elif nota==8898:
        i=False
    else:
        print("No ingresaste una nota valida.")
por1=(apl*100)/n
por2=(apr*100)/n
por3=(prom*100)/n

print("Cantidad de aplazos: ",apl,"(",round(por1,),"%)")
print("Cantidad de aprobados: ",apr,"(",round(por2,),"%)")
print("Cantidad de promocionados: ",prom,"(",round(por3,),"%)")



