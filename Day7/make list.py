import sys

def main():
    f=(x+y for x in range(1,10) for y in range(11,20))
    for x in f:
        print(x)
    #f=[x+y for x in 'abc' for y in range(1,3)]
    #print(f)
    print(sys.getsizeof(f))

if __name__ == "__main__":
    main()
    pass