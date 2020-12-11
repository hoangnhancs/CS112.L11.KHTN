n = int(input().strip())
a = list(map(int, input().strip().split()))

H = [0] * (n + 1)
a = [0] + a

for i in range(1, n + 1):
    H[i] = H[i - 1] + a[i] * (a[i] + 11) * (a[i] + 17)


def get_H(l, r):
    return H[r] - H[l - 1]


ans = []


def solve(x, ans):
    n1 = 0
    n2 = 0
    s1 = -1
    s2 = -1
    for i in range(1, n + 1, x):
        s = get_H(i, i + x - 1)
        if s == s1 or s1 == -1:
            n1 += 1
            s1 = s
        elif s == s2 or s2 == -1:
            n2 += 1
            s2 = s
        else:
            return
    if n1 > 0 and n2 > 0:
        ans += [(x, n1, n2)]


for i in range(1, n):
    if n % i == 0:
        solve(i, ans)

if len(ans) == 0:
    print(-1)
else:
    print(len(ans))
    for x in ans:
        print(*x)