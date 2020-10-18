def acentos(palabra):
    palabra=palabra.lower()
    ac=("á","é","í","ó","ú","ñ","ü")
    cant=0
    for i in ac:
        cant+=palabra.count(i)
    return cant

nombres=["Damian","Agüero","Nicasio","Nicolás","Ñacurutú",]
nombres.sort(reverse=True,key=acentos)
print()
print("Lista ordenada")
for n in nombres:
    print(n)

        
