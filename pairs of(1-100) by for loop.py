
#For loop-সাহায্যে (১-১০০) পযন্ত জোড় সংখ্যা বের করার পদ্ধতিঃ-
for n in range(1,100):
    if(n%2==0):
        print(n)



#For loop-সাহায্যে ১-১০০ পযন্ত বিজোড় সংখ্যা বের করার পদ্ধতিঃ-
for b in range(1,100):
    if(b%2==1):
        print(b)


#Using the for loop and solve the prime numbers:
lower=int(input("Enter lower range:"))
upper=int(input("Enter upper range:"))
print("Prime numbers between",lower,"and",upper,"are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
