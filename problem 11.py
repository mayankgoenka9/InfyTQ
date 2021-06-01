"""
To find number triplets (Three Consecutive Numbers) in an array

"""

n,m=map(int,input().split())
a=[]
for _ in range(n):
    a.append(int(input()))
count=0
for i in range(0,n-2):
    if (a[i+1]*2)==a[i]+a[i+2]:
        count+=1
print(count)
