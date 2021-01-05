n, k = map(int,input().split())
a = list(map(int,input().split()))
a = [0] + a

# prefix sum
for i in range(1,n + 1):
	a[i] += a[i - 1]


# create list b 
b = [0 for _ in range(n - k + 3)]

m = n - k + 1
for i in range(1,n - k + 2):
	b[i] = a[i + k - 1] - a[i - 1]  

# max prefix
pre = [0 for _ in range(n - k + 3)]
for i in range(1,n - k + 2):
	pre[i] = max(b[i],pre[i - 1])

# max suffix
suff = [0 for _ in range(n - k + 3)]
for i in range(n - k  + 1,0,-1):
	suff[i] = max(b[i],suff[i + 1])

ans = 10**15
for i in range(1,m + 1):
	tmp = 0
	if i >= k: tmp = max(tmp,pre[i - k])
	if i + k <= m + 1: tmp = max(tmp,suff[i + k])
	ans = min(ans,tmp)

print(ans)