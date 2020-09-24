from bisect import *
n = int(input())
a, b, c, d = map(int,input().replace('/',' ').split())

points = []
for i in range(0,n):
    x,y = map(int,input().split(' '))
    points.append((x,y))

points = [(c * x - d * y, b * y - a * x) for x, y in points]
points = sorted((x,-y) for x,y in points if x > 0 and y > 0)

# dãy con tăng 

def LIS(A): 
    l = []
    for x,y in A:
        v = bisect_left(l, -y)

        if v == len(l):
            l.append(-y)
        else:
            l[v] = -y

    return len(l)

ans = LIS(points)
print(ans)

# 15
# 1/4 2/1
# 3 1
# 6 2
# 9 3
# 12 4
# 15 5
# 2 1
# 4 2
# 5 3
# 7 4
# 1 3
# 3 4
# 2 5
# 4 5
# 1 6
# 6 6