while True:
    print("\n**Menu**")
    print("1. Count the occurrence of a word in a sentence")
    print("2. Character frequency in a sentence")
    print("3. Display the factors of a given number")
    print("4. Exit")
    choice=input("Enter your choice(1-4): ")
    if choice == '1':
        text=input("Enter a line of text:")
        words=text.split()
        count_words=[]
        counts=[]
        for s in words:
            if s not in count_words:
                count=0
                for i in words:
                    if i==s:
                        count+=1
                count_words.append(s)
                counts.append(count)
        for i in range(len(count_words)):
            print(count_words[i],':',counts[i])
    if choice=="2":    
        words=input("Enter a word:")
        frecounts=[]
        counts=[]
        for s in words:
            if s not in frecounts:
               count=0
               for i in words:
                  if i==s:
                     count+=1
               frecounts.append(s)
               counts.append( count)
        for i in range(len(frecounts)):
            print(frecounts[i],':', counts[i])
    if choice=="3":
         a=int(input("enter a number"))
         if a>=0:
             factors=[]
             for i in range(1,a+1):
                 if a%i==0:
                     factors.append(i)
         print("factors:",factors)
    if choice=="4":
         print("exit")
     

