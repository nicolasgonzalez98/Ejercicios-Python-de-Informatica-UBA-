def muestra(a,b):
    print(a)
    print(b)
    print()

def leeTxt():
    texto=input("Ingrese un texto ")
    return texto
    

def invalidos(text):
    caracteres=(" ",",",";",".",":","-","¿","?","!","¡")
    for car in text:
        if not car.isalpha() and car not in caracteres:
            text.replace(car,"*")
    text.replace("*","")
    t=t.capitalize()
    return t
    
        
    


    
    

texto=leeTxt()
if invalidos(texto):
    t=limpia(texto)
muestra('Texto inicial',texto)
muestra('Texto Modificado',t)
exit()
