def getRTriPat():
    n=int(input("enter no of rows- "))
    print("\n my triangle pattern,")
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(" #* ",end="")
        print()
getRTriPat()
