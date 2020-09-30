sum=0
for i in range (1, 101):
    for j in range (i+1, 101):
        sum += i*j

print(sum*2)