names=["Anu","Meena","Rani","Anand"]
list=[]
for i in names:
    i=i.lower()
    count=0
    for j in i:
        list.append(j)
for k in list:
    if k=='a':
        count+=1
print("Totaloccurences of 'a':",count)
