base=int(input("Ingrese una base impar: "))
n=base//2

while base%2==0:
    base=int(input("Ingrese una base impar: "))
    n=base//2

for i in range(1,base+1,2):
    print(" "*n, end="*"*i)
    print()
    n=n-1

exit()
