#-------------------------std-------------------------
# import numpy as np

n = int(input())
data = list(map(int,input().split(' ')))
a = data 
local_max = []
i = 1;
n = len(data)
start = None
while i != n-2:
    if start is not None:
        pass
    if(a[i-1]<a[i] and a[i+1]<a[i]):
        local_max.append((i-1,i+1))
        i+=1
        start = None
        # print((i-1,i+1))
        continue

    if a[i-1]< a[i] and start == None:
        start = i-1
    if a[i+1]==a[i]:
        start+=1
    if a[i+1] < a[i]:
        # print((start,i+1))
        local_max.append((start,i+1))
        start = None
    i+=1

print(local_max)
