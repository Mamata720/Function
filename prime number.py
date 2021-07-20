def prime_not(num):
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for x in range(2,num):
            if (num%x==0):

                return False
        return True

print(prime_not(10))
#     i=1
#     a=0
#     while num>=i:
#         if num%i==0:
#             print(i)
#             a=a+1
#         i+=1
#     if a==2:
#         print("prime no")
#     else:
#         print("not prime no")
# prime_not(12)
