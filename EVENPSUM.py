t=int(input())
for i in range(t):
    a, b= map(int, input().split())
    aeven=a//2
    beven=b//2    
    bodd=b-beven
    count=aeven*beven
    count= count+((a-aeven)*(b-beven))
    print(count)