def muestra(a,b):
    print(a)
    print(b)
    print()

def leeTxt():
    t=input("Ingrese un texto: ")
    return t

def derecha(text):
    text=list(text)
    texto=[]
    for i in range(len(text)):
        if text[i]>="a" and text[i]<"z":
            texto.append(chr(ord(text[i])+1))
        elif text[i]>="A" and text[i]<"Z":
            texto.append(chr(ord(text[i])+1))
        elif text[i]==" ":
            texto.append(" ")
        elif text[i]=="Z":
            texto.append("A")
        elif text[i]=="z":
            texto.append("a")
        elif text[i]=="Á":
            texto.append("B")
        elif text[i]=="á":
            texto.append("b")
        elif text[i]=="É":
            texto.append("F")
        elif text[i]=="é":
            texto.append("f")
        elif text[i]=="Í":
            texto.append("J")
        elif text[i]=="í":
            texto.append("j")
        elif text[i]=="Ó":
            texto.append("P")
        elif text[i]=="ó":
            texto.append("p")
        elif text[i]=="Ú":
            texto.append("V")
        elif text[i]=="ú":
            texto.append("v")
        else:
            texto.append(text[i])
    texto="".join(texto)
    return texto

def izquierda(text):
    text=list(text)
    texto=[]
    for i in range(len(text)):
        if text[i]>"a" and text[i]<="z":
            texto.append(chr(ord(text[i])-1))
        elif text[i]>"A" and text[i]<="Z":
            texto.append(chr(ord(text[i])-1))
        elif text[i]==" ":
            texto.append(" ")
        elif text[i]=="A":
            texto.append("Z")
        elif text[i]=="a":
            texto.append("z")
        elif text[i]=="Á":
            texto.append("Z")
        elif text[i]=="á":
            texto.append("z")
        elif text[i]=="É":
            texto.append("D")
        elif text[i]=="é":
            texto.append("d")
        elif text[i]=="Í":
            texto.append("H")
        elif text[i]=="í":
            texto.append("h")
        elif text[i]=="Ó":
            texto.append("N")
        elif text[i]=="ó":
            texto.append("n")
        elif text[i]=="Ú":
            texto.append("T")
        elif text[i]=="ú":
            texto.append("t")
        else:
            texto.append(text[i])
    texto="".join(texto)
    return texto


texto=leeTxt()
muestra('Texto inicial',texto)
t1=derecha(texto)
t2=izquierda(texto)
muestra('Texto con Shift a derecha',t1)
muestra('Texto con Shift a izquierda',t2)
    
