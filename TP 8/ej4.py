menu=["flan","arroz","carne con papas","Estrogonoff","bananas",'ñoquis','garrapiñadas']


for i in range(len(menu)):
    menu[i]=menu[i].lower()

print("Comidas entre c y f inclusive: ")

for i in range(len(menu)):
    if menu[i][0]>="c" and menu[i][0]<"g":
        print(menu[i])
