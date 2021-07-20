def chack_number_list(x,y):
    if x%2==0:
        if y%2==0:
            print("x and y both are even number")
        else:
            print("x is even number")
    else:
        print("x is not even number")
x=int(input("enter first number"))
y=int(input("enter second number"))
chack_number_list(x,y)
