def show_numbers(limit):
    i=1
    while i<=limit:
        if i%2==0:
            print(i,"even number")
        else:
            print(i,"odd number")
        i=i+1
a=int(input("enter a number"))
show_numbers(a)
