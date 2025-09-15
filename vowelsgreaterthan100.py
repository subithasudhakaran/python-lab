n=int(input("enter the number range:"))
numbers=[]
for i in range(n):
   i=int(input("enter the number:"))
   if i>100:
       numbers.append('over')
   else:
       numbers.append(i)
print(numbers)       
