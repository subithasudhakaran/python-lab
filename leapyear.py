current_year=int(input("enther the current year:"))
final_year=int(input("enter the final year:"))
print("Leap years")
for i in range(current_year,final_year+1):
   if(i%4==0 and i%100!=0)or(i%400==0):
     print(i)
