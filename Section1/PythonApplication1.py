#a  = [2,-4,5,-8,4,-1,-1,1,1,1,-2,2,4,-6,9,-4]
a = [-3, -22, 1, -9, -7]


max = -9999999999

for i in range(0, len(a)):
    for j in range(0, i+1):
        sum = 0
        for k in range(j,i+1):
            sum+=a[k]
        
        if sum>max:
            max=sum
            print(j+1, i+1, sum)


#a[p]+...+a[q] = (a[0]+...+a[q]) - (a[0]+...+a[p])=summ[q]-summ[p]
#IDEA IS WITH EACH SUMM[I], WE CALCULATE THE SMALLEST CHILDREN LIST START AT THE 1ST ELEMENT. AFTER THAT, WE CALCULATE SUMM[I] SUBTRACT
#THE CORRESPONDING CHILDREN LIST AND FIND THE BIGGEST VALUE OF THIS SUBTRACTION, AND IT IS THE RESULT. 
#THE SMALLEST CHILDREN LIST WE CAN CALCUTE BASE ON PREVIOUS SMALLEST CHILDREN LIST


summ = []       #summ[i] = a[0]+...+a[i]
minn = []       #minn[i] = [min(summ[0],...,summ[i]), index_of_smallest_summ]
maxx = []       #maxx[i] = [summ[i], i]
maxsum = []     #maxsum[i] = [ (maxx[i]-minn[i]), [minn[i][1], maxx[i][1]] ]

#All above of list has same length

summ.append(a[0])                   #sum[0]=a[0] is true 
maxx.append([a[0], 1])              #maxx[0] include a[0]'s value and index 1(because a[0] is the 1st element)
maxsum.append([a[0], [1 , 1]])      #
if(a[0]>=0):
    minn.append([0, 1])
    f_min = 0
else:
    minn.append([a[0], 1])
    f_min = a[0]

f_max = a[0]
max_index = 1
min_index = 1

for i in range(1 ,len(a)):
    summ.append(summ[i-1] + a[i])
    if(f_min > summ[i]):
        f_min = summ[i]
        min_index = i+1
    maxx.append([summ[i], i+1])
    minn.append([f_min, min_index])
    maxsum.append([(maxx[i][0]-minn[i][0]), [minn[i][1]+1, maxx[i][1]]])
'''
for i in range(0, len(summ)):
    maxsum.append()  
'''

print(summ)
print(minn)
print(maxx)
print(maxsum)
'''
print(sum[0], min[0], max[0])
'''
