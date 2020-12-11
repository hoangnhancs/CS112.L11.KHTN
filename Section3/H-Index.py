n = int(input())
arr = list(map(int,input().split(' ')))
def H_index(citations): 
    citations.sort() 
    for i in range(0,len(citations)) : 
        result = len(citations) - i 
        if result <= citations[i]: 
            return result 
           
    return 0
# citation = [50, 40, 33, 23, 12, 11, 8, 5, 1, 0] 

print(H_index(arr)) 