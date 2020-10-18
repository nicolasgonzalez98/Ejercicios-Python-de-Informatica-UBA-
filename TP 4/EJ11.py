import random

valor=('As',2,3,4,5,6,7,8,9,'J','Q','K')
palos=('trebol', 'corazón', 'diamante', 'pica')



mano=set()


while len(mano)<4:
    f=random.randint(0,len(valor)-1)
    g=random.randint(0,len(palos)-1)
    carta=(valor[f], palos[g])
    mano.add(carta)

while len(mano)>0:
    naipe=mano.pop()
    print(naipe[0],"de",naipe[1])
