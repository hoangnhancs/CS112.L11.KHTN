# a = input()
# a = int(a)
# dic_mod = {0:set(), 1:set(), 2:set()}
# cal = a
# list_digit = []
# sum_digit = 0
# while cal!=0:
#     digit = cal%10
#     sum_digit+=digit
#     list_digit.append(digit)
#     cal = cal//10
#     dic_mod[digit%3].add(digit)

# # dic_mod[1].append(1)

# a = {1,3,2,4,9}
# dic_mod[0]=sorted(dic_mod[0])
# dic_mod[1]=sorted(dic_mod[1])
# dic_mod[2]=sorted(dic_mod[2])

# mod = sum_digit%3
# if mod!=0:
#     if dic_mod[mod]:
#         list_digit.remove(dic_mod[mod][0])
#     else:
#         list_digit.remove(dic_mod[3-mod])
#         dic_mod[3-mod].pop(0)
#         list_digit.remove(dic_mod[3-mod])
# list_digit = sorted(list_digit)
# #print(list_digit[::-1])
# for _ in list_digit[::-1]:
#     print(_,end="")

#-------------------NEW_VERSION----------------
# from sys import stdin, stdout
# from collections import Counter

# n = stdin.readline().strip()
# count = Counter(n)
# #print("Count number is: ",count)
# tong = sum(map(int, n)) % 3
# #print(tong)

# # du = [[]] * 3
# # du[1] = ['1', '4', '7']
# # #print(du)
# # du[2] = ['2', '5', '8']
# # #print(du)
# # du = [[x for x in d if x in count] for d in du]
# du = [[]] * 3
# for number in count:
#     number = int(number)
#     if number%3:
#         du[number%3].add(str(number))

# print("Mod number is: ",du)
# #print("Mod is: ",tong)

# if tong:
#     d = sum(count[x] for x in du[tong])
#     #print("Count number of digit has same mod is: ",d)
 
#     c = 1
#     if not d:
#         c = 2
#         tong = 3 - tong
#     # print('Mod become: ',tong)
#     # print("Number digit delete is: ",c)
#     # print("Numbers have mod {} in mod_number is: ".format(tong),du[tong])
#     for x in du[tong]:
#         t = min(c, count[x])
#         c -= t
#         count[x] -= t
    

        
# #print(count)
# #print(count.keys())
# for x in sorted(count.keys(), reverse=True):
#     stdout.write(x * count[x])
# print()

# d=3
# if d:
#     print(d)

#----------------------NEW_VERSION----------------------
from collections import Counter
n = input().strip()
count_number = Counter(n)
#print("Count number is: ",count_number)
# mod_number = {0:set(), 1:set(), 2:set()}
# for number in count_number:
#     number = int(number)
#     if number%3:
#         mod_number[number%3].add(str(number))
mod_number = []
#print(mod_number)
mod_number.append([])
mod_number.append(['1','4','7'])
mod_number.append(['2','5','8'])
mod_number = [[x for x in d if x in count_number] for d in mod_number]
#print("Mod number is: ",mod_number)
sum_digit = sum(int(digit)*count_number[digit] for digit in count_number)
#print("Sum digits is: ",sum_digit)
mod = sum_digit%3
#print("Mod is: ",mod)

if mod:
    # for number in mod_number[mod]:
    #     print(count_number[str(number)])
    count_digit_same_mode = sum(int(count_number[number]) for number in mod_number[mod])
    #print("Count number of digit has same mod is: ",count_digit_same_mode)
    number_digit_delete = 1
    if not count_digit_same_mode:
        mod = 3 - mod   
        number_digit_delete = 2
    # print("Mod become: ",mod)
    # print("Number digit delete is: ",number_digit_delete)
    # print("Numbers have mod {} in mod_number is: ".format(mod),mod_number[mod])
    for _ in mod_number[mod]:
        # print("Count number {} is: ".format(_),count_number[str(_)])
        __ = min(number_digit_delete, count_number[_])
        number_digit_delete -= __
        count_number[_] -= __
#print(count_number)
for _ in sorted(count_number.keys(), reverse=True):
    print(_*count_number[_], end="")



