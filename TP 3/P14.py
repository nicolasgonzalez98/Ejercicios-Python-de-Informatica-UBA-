base=int(input("Ingrese la base: "))
altura=int(input("Ingrese la altura: "))


while base<5 or altura<5:
    print("Ingresaste datos erroneos.")
    base=int(input("Ingrese la base: "))
    altura=int(input("Ingrese la altura: "))

alt=altura-4
bas=base-4

for i in range(1,3):
    print("*"*base)

for b in range(1,alt+1):
    print("**", end=' '*bas)
    print("**")

for f in range(1,3):
    print("*"*base)



