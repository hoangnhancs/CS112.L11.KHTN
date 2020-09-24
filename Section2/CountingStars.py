import time
# nhập 
# n = int(input())
# a, b, c, d = map(int,input().replace('/',' ').split())
n = int(input())
a, b, c, d = map(int,input().replace('/',' ').split())

points = [map(int,input().split()) for _ in range(n)]
rpoints = [(-a*x+b*y,-(-c*x+d*y)) for x,y in points]
spoints = sorted([(x,y) for x,y in rpoints if x>0 and y>0], key=lambda x: (x[0], -x[1]))
new_points = spoints


# def get_points(n):
#     points = []
#     points = [map(int,input().split()) for _ in range(n)]
#     # for i in range(0,n):
#     #     x,y = map(int,input().split()[:2])
#     #     points.append((x,y))
#     return points
# # hết phần nhập, tới phần ánh xạ x, y thành x,y mới         
# def pre_process(points):
#     rpoints = list((-a*x+b*y,-(-c*x+d*y)) for x,y in points)
#     spoints = sorted([(x,y) for x,y in rpoints if x>0 and y>0], key=lambda x: (x[0], -x[1]))
#     return spoints

    
# points = get_points(n)
# points_ = pre_process(points)
# dãy con tăng 
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
array = list(map(lambda x:x[1],new_points))
# start = time.time()
ans = LIS(array,len(array))
# end = time.time()
print(ans)
# print(end - start)

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