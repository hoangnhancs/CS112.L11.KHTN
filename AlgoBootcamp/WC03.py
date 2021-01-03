n = int(input())

list_height = []

for _ in range (n):
    tmp = int(input())
    list_height.append(tmp)

weight_list_height = [-1]*n
i=1
while i<=n-2:
    if list_height[i-1]>list_height[i] or list_height[i+1]>list_height[i]:
        weight_list_height[i]=-1
        i+=1
    else:
        tmp_pos = i+1
        while list_height[tmp_pos]==list_height[i]:
            tmp_pos+=1
        if list_height[tmp_pos]<list_height[i]:
            for _ in range (i, tmp_pos):
                weight_list_height[_]=tmp_pos-i
        else:
            weight_list_height[i]=-1
        #for i in range (i)
        i = tmp_pos

print(weight_list_height)
minn = 9999999999
minn_index=-1
for i in range (n):
    if weight_list_height[i]>=0 and weight_list_height[i]<minn:
        minn=weight_list_height[i]
        minn_index=i
print(minn_index,minn_index+weight_list_height[minn_index]+1)

