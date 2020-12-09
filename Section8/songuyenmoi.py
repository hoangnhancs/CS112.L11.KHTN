def solve(a):
    int_a = int(a)
    list_a = list(a)
    mod = int_a%3

    magic = {
        2:[8,5,2],
        1:[7,4,1],
        3:[9,6,3]
    }
    check=1
    change = 0
    while check!=0:
        #print('mod', mod)
        for i in range (len(list_a)):
            list_a[i] = int(list_a[i])
            #print('with',list_a[i])
            # if list_a[i]!=9 :
            for j in magic[3-mod]:
                #print('check',j)
                if list_a[i]+j<10:
                    #print('has changed')
                    list_a[i]=list_a[i]+j
                    change=1
                    check=0
                    break
            if check ==0:
                break
        check=0

    if change==0:
        #print("change...")
        if mod!=0:
            list_a[-1] = int(list_a[-1])-mod
        else:
            list_a[-1] = int(list_a[-1])-3

    return ''.join([str(x) for x in list_a])
print(solve(a))

