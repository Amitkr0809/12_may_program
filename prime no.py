n= int(input("enter number :"))

for i in range(1, n+1):
    if i > 1: # Prime numbers are greater than 1
        for j in range(2, i):
            if (i % j) == 0:
                # print(i,"is a composite number")
                break
        else:
            print(i,"is a prime number")
