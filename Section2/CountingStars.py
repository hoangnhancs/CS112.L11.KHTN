# n = int(input())
# a, b, c, d = map(int,input().replace('/',' ').split())

# def get_points(n,a,b,c,d):
#     points = []
#     for i in range(0,n):
#         x,y = map(int,input().split()[:2])
#         points.append((x,y))
#     return points
        
# def pre_process(points):
#     rpoints = list((-a*x+b*y,-(-c*x+d*y)) for x,y in points)
#     spoints = sorted([(x,y) for x,y in rpoints if x>0 and y>0], key=lambda x: (x[0], -x[1]))
#     return spoints

    
# points = get_points(n,a,b,c,d)
# a = pre_process(points)


# print(a)
import time
n = int(input())
a, b, c, d = map(int,input().replace('/',' ').split())

def get_points(n,a,b,c,d):
    points = []
    for i in range(0,n):
        x,y = map(int,input().split()[:2])
        points.append((x,y))
    return points
        
def pre_process(points):
    rpoints = list((-a*x+b*y,-(-c*x+d*y)) for x,y in points)
    spoints = sorted([(x,y) for x,y in rpoints if x>0 and y>0], key=lambda x: (x[0], -x[1]))
    return spoints

    
points = get_points(n,a,b,c,d)
points_ = pre_process(points)
    
def bin_search(A, l, r, key): 
    while (r - l > 1): 
      
        m = l + (r - l)//2
        if (A[m] >= key): 
            r = m 
        else: 
            l = m 
    return r 
   
def LIS(A, size): 
  
    # Add boundary case, 
    # when array size is one 
   
    tailTable = [0 for i in range(size + 1)] 
    leng = 0 # always points empty slot 
   
    tailTable[0] = A[0] 
    leng = 1
    for i in range(1, size): 
      
        if (A[i] < tailTable[0]): 
  
            # new smallest value 
            tailTable[0] = A[i] 
   
        elif (A[i] > tailTable[leng-1]): 
  
            # A[i] wants to extend 
            # largest subsequence 
            tailTable[leng] = A[i] 
            leng+= 1
   
        else: 
            # A[i] wants to be current 
            # end candidate of an existing 
            # subsequence. It will replace 
            # ceil value in tailTable 
            tailTable[bin_search(tailTable, -1, leng-1, A[i])] = A[i] 
          
   
    return leng
  

# array = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60] 
array = list(map(lambda x:x[1],points_))
start = time.time()
ans = LIS(array,len(array))
end = time.time()
print(ans)
print(end - start)






# # from bisect import *

# n = int(input())
# a, b, c, d = map(int,input().replace('/',' ').split())

# points = [map(int,input().split()) for _ in range(n)]
# rpoints = [(-a*x+b*y,-(-c*x+d*y)) for x,y in points]
# print(rpoints)
# spoints = sorted([(x,y) for x,y in rpoints if x>0 and y>0], key=lambda x: (x[0], -x[1]))
# print(spoints)
# f = []
# for x,y in spoints:
#     print(f)
#     i = bisect_left(f,y)
#     if i == len(f):
#         f.append(y)
#     else:
#         f[i] = y
# print(f)
# print(len(f))

# n = int(input())
# a, b, c, d = map(int,input().replace('/',' ').split())

# def get_points(n,a,b,c,d):
#     points = []
#     for i in range(0,n):
#         x,y = map(int,input().split()[:2])
#         points.append((x,y))
#     return points
        
# def my_key(point):
#     x = point[0]
#     y = point[1]
#     return (c*x - d*y,a*x - b*y)

# points = get_points(n,a,b,c,d)
# points.sort(key=my_key)
# print(points)

# -------------------



# 
# n = int(input())
# a,c = input().split()[:2]
# a,b = a.split('/')
# c,d = c.split('/')

# a=int(a)
# b=int(b)
# c=int(c)
# d=int(d)

# points = []

# for i in range(1,n+1):
# 	x,y = map(int,input().split()[:2])
# 	if b*y-a*x > 0 and d*y-c*x < 0:
# 		points.append((x,y))

# def mykey(x):
# 	return (c*x[0] - d*x[1],a*x[0] - b*x[1])
# print(points)
# points.sort(key=mykey)
# print(points)
# lis = []
# for point in points:
# 	low = 0
# 	high = len(lis) - 1
# 	ret = 0
# 	while low <= high:
# 		mid = (low + high)//2
# 		if lis[mid] < b*point[1] - a*point[0]:
# 			ret = mid + 1
# 			low = mid + 1
# 		else:
# 			high = mid - 1
# 	if ret == len(lis):
# 		lis.append(b*point[1] - a*point[0])
# 	else:
# 		lis[ret] = b*point[1] - a*point[0]
# print(lis)
# print(len(lis))