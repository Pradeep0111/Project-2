n=int(input("Enter the range for the Fibonacci series:"))
num=0
num1=1
sum=0
for i in range(n):
    print(sum,end=" ")
    num=num1
    num1=sum
    sum = num+num1
