ending = input()
ending = int(ending)
i=2
while (ending!=1):  
    if (ending%i==0):
        ending/=i
        print(i)
        i=2
    else:
        i+=1

print(ending)