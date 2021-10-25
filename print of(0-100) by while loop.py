 ১ থেকে ১০০ পযন্ত যোগ করার প্রোগ্রাম।
sum=0
n=1
while n<=100:
    sum=sum+n
    n=n+1
print("The result is:")
print(sum)
# ১ থেকে ১০০ পযন্ত প্রিন্ট করার প্রোগ্রাম।
a=1
while a<=100:
    print(a)
    a=a+1
print("This is an end")
# ১ থেকে ১০০ পযন্ত জোড় সংখ্যা প্রিন্ট করার প্রোগ্রাম।
for n in range (1,100):
    if(n%2==0):
        print(n)
# লিস্টের সংখ্যাগুলো যোগ করার প্রোগ্রাম।
num=[1,2,3,4,5,6,7,8,9]
sum=0
i=0
while i<=8:
    sum=sum+num[i]
    i=i+1
print(sum)
