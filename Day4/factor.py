a=int(input("Enter a:"))
b=int(input("Enter b:"))
if a>b:
    a,b=b,a
r=1
while r!=0:
    r=b%a
    b=a
    a=r
print("factor:%d"%(b))