from sys import stdin,stdout

input_s = stdin.readline()
input_s = input_s.strip()
n =int(stdin.readline())
value = {}
for i in range(97,123):
    value[chr(i)]= 1<<i-97
# print(value)
sums = [0 for _ in range(len(input_s)+1)]

for i in range(len(input_s)):
    sums[i+1] = sums[i] + value[input_s[i]]
# print(sums)

for i in range(n):
    a,b,c,d = map(int,stdin.readline().strip().split(' '))
    # print(sums[b], sums[a - 1])
    # print(sums[d], sums[c - 1])
    if(sums[b]-sums[a-1]==sums[d]-sums[c-1]):
        stdout.write('YES\n')
    else:
        stdout.write('NO\n')