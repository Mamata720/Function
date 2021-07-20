def num(name):
    a=0
    i=0
    while i<len(name):
        if a<len(name[i]):
            a=len(name[i])
            c=name[i]
        i=i+1
    print(c)
num(["mamta","subhashini","priyanka"])
