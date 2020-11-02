genA = input().strip().upper()
genB = input().strip().upper()
# genA = 'ABBACAB'
# genB = 'BCABB'
temp = set()
# gen =None
# gen = genA if len(genA) > len(genB) else genB
count = 0
for i in range(len(genB)-1):
    pair = genB[i:i+2]
    temp.add(pair)
# print(temp)
for i in range(len(genA)-1):
    pair = genA[i:i + 2]
    # print(pair)
    if pair in temp:
        count+=1
print(count)
