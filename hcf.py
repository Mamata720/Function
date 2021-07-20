def mamta_rajput(x,y):
    
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    print(hcf)
num=int(input("enter a number:"))
num1=int(input("enter a number:"))
print("hcf of",num,"and",num1,"is",mamta_rajput(num,num1))
