#import math
dict_vt = {}
n = int(input())
for _ in range (2*n):
    a, b = map(int, input().split())
    dict_vt[_] = [a, b]

dict_vt_sorted = sorted(dict_vt.items(), key=lambda k: abs(k[1][0]-k[1][1]))
#print(dict_vt_sorted)
s = t = n
sum_res=0
dict_vt_sorted = dict_vt_sorted[::-1]
for i in range (2*n):
    if dict_vt_sorted[i][1][0]>dict_vt_sorted[i][1][1]:
        sum_res+=dict_vt_sorted[i][1][0]
        s-=1
        
    else:
        sum_res+=dict_vt_sorted[i][1][1]
        t-=1
    pos = i
    if s==0 or t==0:
        break

if s==0:
    for i in range (pos+1, 2*n):
        sum_res+=dict_vt_sorted[i][1][1]
else:
    for i in range (pos+1, 2*n):
        sum_res+=dict_vt_sorted[i][1][0]

print(sum_res)

    
