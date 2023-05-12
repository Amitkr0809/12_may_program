# 1  Armstrong number

num = input("enter number : ")
n = len(num)
sum = 0
for i in num :
    sum = sum + int(i) ** n
print (sum)

if sum == int(num):
    print("given number",num, "is armstrong number")
else:
    print("given number",num, "is not armstrong number")


