def aad_number_list(x,y):
    i=0
    j=0
    d=[]
    while i<len(x):
        while j<len(y):
            s=x[i]+y[j]
            d.append(s)
            break
        j=j+1
        i=i+1
    print(d)
a=[50,60,10]
b=[10,20,13]
aad_number_list(a,b)
