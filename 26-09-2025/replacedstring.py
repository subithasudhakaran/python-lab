a=input("enter a string:")
firstchar=a[0]
result=firstchar+a[1:].replace(firstchar,"$")
print(result)
    
