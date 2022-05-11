n=int(input("Enter the number: "))
sum=0
i=n
while i>0:
    d=i%10
    sum=sum+d**3
    i=i//10
if n==sum:
    print(n," is an armstrong number")
else:
    print(n," is not an armstrong number")