n=int(input("Enter a number:"))
i=n
sum=0
while(i>0):
    r=i%10
    sum=sum+r*r*r
    i=int(i/10)
if(sum==n):
    print("Armstrong")
else:
    print("Not Armstrong")    

