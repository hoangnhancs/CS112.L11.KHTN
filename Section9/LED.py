n = int(input())

mod = n%3
if mod == 1:
    print(7*(n//3 - 1) + 4)
elif mod == 0:
    print(7*(n//3))
elif mod == 2:
    print(7*(n//3) +  1)