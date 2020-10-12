import time
start=time.time()
has2={}
def collatz(x):
    seq=[]
    seq.append(x)
    temp=x
    while(temp>1):
        if temp%2==0:
            temp=int(temp/2)
            if temp in has2:
                seq+=has2[temp]
                break
            else:
                seq.append(temp)
        else:
            temp=3*temp+1
            if temp in has2:
                seq+=has2[temp]
                break
            else:
                seq.append(temp)


    has2[x]=seq            
    return len(seq)

num=0
greatest=0
for i in range(1000000):
    c=collatz(i)
    if num<c:
        num=c
        greatest=i
print('{0} has {1} elements. calculation time ={2} seconds.'.format(greatest,num,time.time()-start))