
phi=int(input())
for i in range(phi):
    y=list(map(int, input().split()))
    n=y[0]
    d=y[1]
    ris=0
    nris=0
    ls=list(map(int, input().split()))
    if d==1:
        print(n)
    else:
        for i in ls:
            if i>=80 or i<=9:
                ris+=1
        nris=n-ris
        count=0
        if ris%d==0:
            count=count+(ris//d)
        else:
            count=count+(ris//d)
            count +=1
        
        if nris%d==0:
            count=count+(nris//d)
        else:
            count= count+ (nris//d)
            count+=1
        print(count)