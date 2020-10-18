def ord_alf(l):
    for i in range(len(l)):
        l[i]=l[i].capitalize()
    l.sort()
    return l
    





nom_fem=["maria", "elsa", "aurora","antonia","Rocio","iara","tabatha","milena","Florencia","roxana","martha","magali","carolina","romina","marcela","susana","frida","mariana","martina","Roberta"]
##nom_masc=["nicolas","felix","franco","fabian","matias","gabriel","angel","agustin","tiago","Antonio","diego","lionel","leonel","ricardo","alexis","cristian","Rodrigo","Martin","Floki","ragnar"]

##for i in range(len(nom_masc)):
##    nom_masc[i]=nom_masc[i].capitalize()

for i in range(len(ord_alf(nom_fem))):
    print(ord_alf(nom_fem)[i])
    




