print('Los 4 primeros numeros perfectos son:')
print(6)
cant=1
num=7
while cant<4:
    sumador=1
    for j in range(2,(num//2)+1):
        if num%j==0:
            sumador+=j
    if sumador==num:
        print(num)
        cant+=1
    num+=1
exit()
