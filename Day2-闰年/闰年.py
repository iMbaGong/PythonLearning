year=int(input('Enter the year:'))
res=year%4 and year%100!=0 or year%400
print(res is True)