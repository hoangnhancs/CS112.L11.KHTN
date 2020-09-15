a = []
a.append(1)
a.append(2)
i = 1
sum = 2
while (a[i-1]+a[i])<=4000000:
    a.append((a[i-1]+a[i]))
    i+=1
    if a[i]%2==0:
        sum+=a[i]

print(sum)
