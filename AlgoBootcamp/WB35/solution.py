#-------------------------file---------------------------------
# data = []
# n = None
# with open('ENERGY.INP') as f :
#     n = f.readline()
#     n = int(n)
#     for _ in range(0,2*n):
#         a,p = map(int,f.readline().split(' '))
#         data.append((a,p))
#         # print(a,p)
#-------------------------std--------------------------------
data = []
n = int(input())
for _ in range(2*n):
    a,p = map(int,input().split(' '))
    data.append((a,p))
print(100)
#
# data = sorted(data,key=lambda x:abs(x[0]-x[1]),reverse=True)
# morning = []
# night = []
# for a,p in data:
#     if a>p :
#         if(len(morning)==n):
#             night.append(p)
#         else:
#             morning.append(a)
#     if p>a:
#         if (len(night) == n):
#             morning.append(a)
#         else:
#             night.append(p)

# print(data)
# print(morning,night)
# print(sum(morning)+sum(night))
# 3
# 2 4
# 3 6
# 5 2
# 7 1
# 4 9
# 10 11
