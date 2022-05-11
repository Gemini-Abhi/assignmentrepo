p=int(input("Enter the  principal amount: "))
t=int(input("Enter the  time: "))
r=float(input("Enter the  rate: "))
a= p*(pow((1+r/100),t))
c= a - p
c=float(c)
print("Compound interest is %d " %c)