l1=[]

while len(l1)<20:
    num=int(input("Ingrese un numero entero positivo: "))
    if num>0:
        l1.append(num)

l2=[]

for i in range(0,len(l1)):
    num=l1[i]
    if num not in l2:
        l2.append(num)


print("Lista definitiva")
print()

print(l2)
