from random import randint
loop_count = 5
n = input()
n = int(n)
k = 0
def check(n):
    return not (n < 2 or
                any(pow(randint(1, n - 1), n - 1, n) != 1
                    for _ in range(loop_count)))
        
sum = 0
for i in range (2, 2000001):
    if check(i):
        sum += i


print(sum)
