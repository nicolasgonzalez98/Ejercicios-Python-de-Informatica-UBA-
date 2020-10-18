num=int(input("Ingrese un numero de 4 cifras: "))

if num>=1000 and num<=9999:
    c1=num//1000
    c2=(num%1000)//100
    c3=(num%100)//10
    c4=(num%10)
    print(c1,"-",c2,"-",c3,"-",c4)
    
else:
    print("Ingresaste un numero invalido.")
    
