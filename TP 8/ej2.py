def ord_alf(l):
    for i in range(len(l)):
        l[i]=l[i].lower()
    l.sort()
    return l

def comb_lista(a,b):
    total=a+b
    return total

nom_masc=["nicolas","felix","franco","fabian","matias","gabriel","angel","agustin","tiago","Antonio","diego","lionel","leonel","ricardo","alexis","cristian","Rodrigo","Martin","Floki","ragnar"]
nom_fem=["maria", "elsa", "aurora","antonia","Rocio","iara","tabatha","milena","Florencia","roxana","martha","magali","carolina","romina","marcela","susana","frida","mariana","martina","Roberta"]
ord_alf(nom_masc)
ord_alf(nom_fem)

total=comb_lista(nom_fem,nom_masc)

print(total)


