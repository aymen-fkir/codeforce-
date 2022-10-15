num=input()
num=num.split(" ")
n=int(num[0])
m=int(num[1])
a=int(num[2])

def the(n,m,a):
    if n>=m:
        longeur=n
        houteur = m
    else:
        longeur = m
        houteur = n

    if longeur % a == 0:
        long = longeur // a
    else:
        long = longeur // a + 1
    if houteur % a == 0:
        cont = houteur // a
    else:
        cont = houteur// a + 1

    return (long*cont)

print(the(n,m,a))