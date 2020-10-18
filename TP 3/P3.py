dig=int(input("Ingrese el digito a contar: "))
i=1
cant=0

if dig>=0 and dig<=9:
    while i<11:
        num=int(input("Ingrese el numero %s: "%i))
        c1=num//10000
        c2=(num%10000)//1000
        c3=(num%1000)//100
        c4=(num%100)//10
        c5=num%10
        if num>9999 and num<=99999:
            if c1==dig:
                cant=cant+1
            if c2==dig:
                cant=cant+1
            if c3==dig:
                cant=cant+1
            if c4==dig:
                cant=cant+1
            if c5==dig:
                cant=cant+1
            i=i+1
        else:
            print("Ingresaste un numero invalido")
else:
    print("Ingresaste un digito invalido.")

print("el digito",dig,"aparece",cant,"veces")
