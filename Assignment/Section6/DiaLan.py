# n, k = map(int, input().strip().split())
# a = list(map(int, input().strip().split()))

# result = a[0]

# for i in range (1, len(a)):
#     result = result & a[i]

# if result == 0:
#     print('YES')
# else:
#     print('NO')

# print(4 & 5 & 3)
# result = 3
# for i in [4,5]:
#     result = result & i

# print(64 & 15)

# n, k = map(int, input().strip().split())
# a = list(map(int, input().strip().split()))

# if (k >= 12):
#     t = a[0]
#     for i in a:
#         t = (t & i)
#     if (t==0):
#         print("YES")
#     else:
#         print("NO")
    
# else:
#     flag = True
#     for i in range(n - k + 1):
#         if (flag == False):
#             break
#         t = a[i]
#         for j in range(k):
#             t = (t & a[i + j])
#         if (t == 0):
#             flag = False
#             break
#     if (flag == False):
#           print("YES")
#     else:
#           print("NO")
def search_bit_zeros(a):

    bit_zeros = []
    bin_a = bin(a)[2:]
    bin_a_reseved = bin_a[::-1]
    for i in range (len(bin_a_reseved)):
        if bin_a_reseved[i]=='0':
            bit_zeros.append(i)

    return bit_zeros

n, k = map(int, input().strip().split())
a = list(map(int, input().strip().split()))


max_a = max(a)
#print(max_a)
min_a = min(a)
#print(min_a)
max_length = len(bin(max_a)[2:])
#print(max_length)
min_length = len(bin(min_a)[2:])
#print(min_length)


check = [i for i in range(max_length)]

difference_bit = [i for i in range(min_length, max_length)]

res = set(difference_bit)
count = 0

for _ in a:
    tmp=res.copy()
    print(tmp)
    print(res)
    if tmp.update(search_bit_zeros(_))!=res:
        res = tmp
        count += 1
    print(tmp)
    print(res)
    # if count<=k:
    #     if res==check:
    #         print('YES')
    #         break
    # else:
    #     print('NO')
    #     break