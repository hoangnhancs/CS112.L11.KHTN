import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (d*a - c*b)%(c-d) != 0 or (d*a - b*c)>0:
    print(0)
else: 
    upper_bound = (d*a - c*b)//(c-d)
    count = 0
    while (a*d!=b*c):
        a = a + 1
        b = b + 1
        gcd = math.gcd(a,b)
        a = a//gcd
        b = b//gcd
        count = count +1
        if count > upper_bound:
            break
    if count > upper_bound:
        print(0)
    else:
        print(count)