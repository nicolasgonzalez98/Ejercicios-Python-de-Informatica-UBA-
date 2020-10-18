dd=int(input("Ingrese el día: "))
mm=int(input("Ingrese el mes: "))
yy=int(input("Ingrese el año: "))

if mm>12 or dd>31:
    print("Esta fecha es incorrecta.")
elif mm<1 or dd<1:
    print("Esta fecha es incorrecta.")
elif mm==4 or mm==6 or mm==9 or mm==11 and dd>30:
    print("Esta fecha es incorrecta.")
elif mm==2 and dd>29:
    print("Esta fecha es incorrecta.")
elif mm==2 and dd>28:
    if yy%100!=0 and yy%400==0:
        print("Esta fecha es correcta.")
    if yy%4==0:
        print("Esta fecha es correcta.")
    else:
        print("Esta fecha es incorrecta.")
else:
    print("Esta fecha es correcta.")
        


    

    

    
