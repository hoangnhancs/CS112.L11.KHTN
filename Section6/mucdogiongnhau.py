genA = input()
genB = input()
dic_2_genA = {}
dic_2_genB = {}
for i in range (len(genA)-1):
    t = genA[i:i+2]
    try:
        dic_2_genA[t]+=1
    except:
        dic_2_genA[t]=1
for i in range (len(genB)-1):
    t = genB[i:i+2]
    try:
        dic_2_genB[t]+=1
    except:
        dic_2_genB[t]=1
sum = 0
# print(dic_2_genA)
# print(dic_2_genB)
for _ in dic_2_genA:
    if _ in dic_2_genB:
        sum += dic_2_genA[_]*dic_2_genB[_]
print(sum)