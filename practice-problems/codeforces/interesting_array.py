def isInteresting(a,k):
    return max(a)-min(a)>=k
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    f=0
    for i in range(n):
        for j in range(i+1,n):
           # print(l[i:j+1],l,i,j)
            if len(l[i:j+1])>1 and isInteresting(l[i:j+1],n):
                f=1
                break
        if f==1:
            break
    if f==1:
        print("YES")
        print(i+1,j+1)
    else:
        print("NO")
        