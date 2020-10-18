##ej 3.16

diag=int(input("Ingrese una diagonal impar: "))
n=diag//2

while diag%2==0:
    diag=int(input("Ingrese una diagonal impar: "))
    n=diag//2

for i in range(1,diag+1,2):
    print(" "*n, end="*"*i)
    print()
    n=n-1

n=1
val=diag-4
for i in range(diag-2,0,-2):
    if i==1:
        print(" "*n,'*',' '*val)
        break
    print(" "*n,'*',' '*val,end='*')
    print()
    n=n+1
    val=val-2
