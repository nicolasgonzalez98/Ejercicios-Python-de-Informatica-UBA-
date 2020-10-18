text=input("Ingrese texto:")
text=list(text)
texto=[]

for i in range(len(text)):
    if text[i]>="a" and text[i]<"z":
        print(chr(ord(text[i])+1),end="")
    elif text[i]>="A" and text[i]<"Z":
        print(chr(ord(text[i])+1), end="")
    elif text[i]==" ":
        print(" ",end="")
    elif text[i]=="Z":
        print("A",end="")
    elif text[i]=="z":
        print("a",end="")
    else:
        print(text[i],end="")

