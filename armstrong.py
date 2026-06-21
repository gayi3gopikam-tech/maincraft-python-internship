n=int(input("enter a num:"))
temp=n
sum=0
while temp>0:
    digit = temp % 10
    sum +=digit ** 3
    temp//=10
if sum==n:
    print("armstrong")
else:
    print("not an armstrong")        
