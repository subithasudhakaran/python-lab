num=int(input("enter a positive number"))
factorial=1
if num>0:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial is:",factorial)    

else:
    print("invalid")
    
