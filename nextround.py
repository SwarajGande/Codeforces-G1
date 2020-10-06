n,k = map(int,input().split())
a = list(map(int,input().split()))
c = 0
for i in range(len(a)):
    if (a[i]>0):
        if(a[i]>=a[k-1]):
            c+=1
    else:
        c=c+0
print(c)
