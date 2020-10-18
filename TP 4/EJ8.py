t=input("Ingrese un texto: ")

n=True

while len(t)<71:
    for i in range(len(t)):
        t=t+t[i]

print(t)
