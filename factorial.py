#usingloop
num=int(input("enter a number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print("factorial",fact)

#factorial using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print("factoial",factorial(5))