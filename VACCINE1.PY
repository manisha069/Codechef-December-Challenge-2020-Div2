d1, v1, d2, v2, p=map(int, input().split())

curr_p=0
di=0
count=0
while(curr_p <= p):
    di+=1
    if di >= d1 and di>= d2:
        curr_p += v1+v2
    elif  di >= d1 and di < d2:
        curr_p += v1
    elif di >= d2 and di < d1:
        curr_p += v2
    count+=1
    if( curr_p==p):
        break

print(count)