for i in range(1000,10000):
    c1=i//1000
    c2=(i//100)%10
    c3=(i//10)%10
    c4=i%10
    if c1+c3==c2+c4:
        print(i)
