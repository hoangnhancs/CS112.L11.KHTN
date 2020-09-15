# bài toán này sẽ là bài toán tìm bội chung nhỏ nhất
# ý tưởng là ta sẽ phân tích các số từ 1 đến 20 ra thừa số nguyên tố  (sẽ bao gồm các cơ số và số mũ)
# ta sẽ lưu dưới dạng dict vào biến tạm _dict_temp , rồi ta so sánh với dict chính là biến _dict, xem thử cơ số đó đã có trong _dict hay chưa
# nếu có rồi thì sẽ cập nhập số mũ lớn nhất cho cơ số đó, nếu chưa thì thêm cơ số và số mũ vào _dict
# đó là một cách tìm bội chung lớn nhất đơn giản
# cách này khá cùi bắp và chả ai xài :D

_dict = {}
result = 1

for i in range (2, 21):
    number = i
    div = 2
    _dict_temp = {}

    while (number!=1):  
        if (number%div==0):
            number/=div
            if div in _dict_temp:
                _dict_temp[div] += 1
            else:
                _dict_temp[div] = 1
            div=2
        else:
            div+=1
   

    for x, y in _dict_temp.items():
        if x in _dict:
            if _dict_temp[x] > _dict[x]:
                _dict[x] = _dict_temp[x]
        else:
            _dict[x] = _dict_temp[x]
 


print(_dict)

for x, y in _dict.items():
    result *= pow(x, y)
print(result)

#cách này sử dụng giải thuật euclid để tìm bội chung nhỏ nhất

result2 = 1

def ucln(a, b):
    if (b == 0):
        return a
    return ucln(b, a % b)
 
def bcnn(a, b):
    return int((a * b) / ucln(a, b))

for i in range (2, 21):
    
    result2 = bcnn(result2, i)
    

print(result2)


