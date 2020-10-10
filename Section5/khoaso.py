a = input()
a = int(a)
dic_mod = {0:set(), 1:set(), 2:set()}
cal = a
list_digit = []
sum_digit = 0
while cal!=0:
    digit = cal%10
    sum_digit+=digit
    list_digit.append(digit)
    cal = cal//10
    dic_mod[digit%3].add(digit)

# dic_mod[1].append(1)

a = {1,3,2,4,9}
dic_mod[0]=sorted(dic_mod[0])
dic_mod[1]=sorted(dic_mod[1])
dic_mod[2]=sorted(dic_mod[2])

mod = sum_digit%3
if mod!=0:
    if dic_mod[mod]:
        list_digit.remove(dic_mod[mod][0])
    else:
        list_digit.remove(dic_mod[3-mod])
        dic_mod[3-mod].pop(0)
        list_digit.remove(dic_mod[3-mod])
list_digit = sorted(list_digit)
#print(list_digit[::-1])
for _ in list_digit[::-1]:
    print(_,end="")




