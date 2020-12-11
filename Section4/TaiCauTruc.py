from sys import stdin, stdout
import sys
sys.setrecursionlimit(10**6)
t = stdin.readline().split()
n,m = [int(x) for x in t]
a = [[] for _ in range(n)]
c = [[] for _ in range(n)]
d = [0 for _ in range(n)]
f = [[] for _ in range(n)]
cha = [0 for _ in range(n)]
def dfs(i):
    for j in range(len(a[i])):
        v = a[i][j]
        if (cha[v]==-1):
            #print(v,i)
            cha[v]=i
            d[v] = d[i] + 1
            c[i][j] = 1
            dfs(v)
def dfs2(i):
    for j in range(len(a[i])):
        v = a[i][j]
        if (cha[v]==i):
            d[v] = d[i] + 1
            #print(v,i)
            c[i][j] = 1
            dfs2(v)
def lca(x,y):
    if x==y:
        return x
    if d[x]>d[y]:
        t=x
        x=y
        y=t
    t=d[y]-d[x]
    for i in range(21,-1,-1):
        if 2**i<=t :
            t-=2**i
            y=f[y][i]
    if x==y :
        return x
    for i in range(21,-1,-1):
        if f[x][i]!=f[y][i]:
            x=f[x][i]
            y=f[y][i]
    return f[x][0]
for i in range (m):
    t = stdin.readline().split()
    x,y = [int(x) for x in t]
    a[x-1].append(y-1)
    c[x-1].append(0)
    cha[y-1] = cha[y-1] + 1
s = -1
for i in range(n):
    if (cha[i] == 0):
        if (s != -1):
            print("No")
            exit()
        s = i
#print(s)
if (s == -1):
    print("No")
    exit()
for i in range(n):
    cha[i] = -1
cha[s] = -2
dfs(s)
for i in range(n):
    if (cha[i] == -1):
        print("No")
        exit()
for i in range(n):
    f[i].append(cha[i])
for j in range(1,22):
    for i in range(n):
        f[i].append(f[f[i][j-1]][j-1])
for i in range(n):
    for j in range(len(a[i])):
        if c[i][j] == 0:
            #print(i,a[i][j])
            if  lca(a[i][j],i) != i:
                cha[a[i][j]] = i
for i in range(n):
    for j in range(len(c[i])):
        c[i][j] = 0
dfs2(s)
for i in range(n):
    f[i][0] = cha[i]
for j in range(1,22):
    for i in range(n):
        f[i][j] = f[f[i][j-1]][j-1]
for i in range(n):
    for j in range(len(a[i])):
        #print(i,a[i][j],c[i][j])
        if c[i][j] == 0:
            if  lca(a[i][j],i) != i:
                print("No")
                exit()
print("Yes")
for i in cha:
    print(i+1,end = ' ')