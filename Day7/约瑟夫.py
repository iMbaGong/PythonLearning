def main():
    que=[1]*30
    w=0
    index=0
    num=15
    while True:
        if que[index%30]!=0:
            w+=1
            if w%9==0:
                que[index%30]=0
                num-=1
                if(num==0):
                    break
        index+=1
        
    print(que)

if __name__ == "__main__":
    main()