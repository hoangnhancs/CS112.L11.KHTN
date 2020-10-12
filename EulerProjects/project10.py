def check (n, arr_prime):
  for i in arr_prime:
    if n%i==0:
      return False
  return True
arr_prime = [2]
sum =2
for i in range(3, 2000001):
  if check(i, arr_prime)==True:
    arr_prime.append(i)
    sum+=i
print(sum)

#print(arr_prime)
# #print(check(3,arr_prime))
# print(check(9, arr_prime))