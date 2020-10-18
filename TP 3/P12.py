base=int(input("Ingrese la base: "))
n=base-1

for i in range(1,base+1):
    print(" "*n, end="*"*i)
    print()
    n=n-1
