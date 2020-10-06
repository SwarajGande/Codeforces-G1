l = list(map(int,input().split()))
sum=0
for i in range(len(l)):
    sum=l[i]+sum
if sum%2==0:
    print("YES")
else:
    print("NO")
