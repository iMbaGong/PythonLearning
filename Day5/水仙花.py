for x in range(101,1000):
    val=(x//100)**3+((x%100)//10)**3+(x%10)**3
    #print("%d:%d"%(x,val))
    if x==val:
        print(x)
