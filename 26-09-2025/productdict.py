mydict={"a":2,"b":2,"c":4,"d":10}
total=sum(mydict.values())
result=1
for value in mydict.values():
    result*=value
print("The product of all items in the dictionary",result)
