n,h=list(map(int,input().split()))
a=[]
width=0
for i in range(n):
    k=int(input())
    a.append(k)
for i in range(len(a)):
    if (a[i]<=h):
        width=width+1
    else:
        if (a[i]>h):
            width=width+2
print(width)
