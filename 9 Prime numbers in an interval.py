
u=int(input("Enter the upper value: "))
l=int(input("Enter the lower value: "))
for i in range(u, l + 1):
    if i>1:
        for a in range(2,i):
            if (i % a) == 0:
                break
        else:
            print(i)