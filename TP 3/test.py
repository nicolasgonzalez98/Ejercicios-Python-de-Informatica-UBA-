digito=int(input('Ingrese el dígito a contar: '))
while (digito<0) or (digito>9):
    digito=int(input('Ingrese el dígito a contar: '))
cant=0
print('Ingresar 10 números de 5 cifras')
for i in range(1,11):
    num=int(input('Ingrese el número %d: '%i))
    while (num < 10000) or (num > 99999):
      num=int(input('Ingrese el número %d: '%i))
    divisor=10000
    while num>0:
        dig=num//divisor
        if dig==digito:
            cant+=1
        num%=divisor
        divisor/=10
print()
print('El dígito',digito,'aparece',cant,'veces')
exit()
