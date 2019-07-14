import math
value=int(input("Enter a number:"))
end=int(math.sqrt(value))+1
is_prime=False
for x in range(2,end):
    if value%x:
        is_prime=True
        break;
print(is_prime)