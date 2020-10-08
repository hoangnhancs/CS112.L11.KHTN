# a,k,b,m,n = map(int, input().split())
a, k, b, m, n = map(int, input().split())
 
sum=0
#result = int(n/(a+b))
result = int(n//((1-1/k)*a+(1-1/m)*b)) - 2
while(sum<n):
    sum = (result - int(result//k))*a + (result - int(result//m))*b
    result+=1

print(result-1)