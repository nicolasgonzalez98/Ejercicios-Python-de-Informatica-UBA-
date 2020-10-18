num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
op=int(input("Ingrese la operacion (1+ 2- 3* 4//): "))


if op==1:
    print(num1,"+",num2,"=",num1+num2)
elif op==2:
    print(num1,"-",num2,"=",num1-num2)
elif op==3:
    print(num1,"*",num2,"=",num1*num2)
else:
    print(num1,"//",num2,"=",num1//num2)

    
    

