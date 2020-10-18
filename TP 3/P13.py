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
for i in range(diag-2,0,-2):
    print(" "*n, end="*"*i)
    print()
    n=n+1
    
