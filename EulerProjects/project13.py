f = open('/content/50digits-number.txt', 'r')
data = f.read()
_ = data.split('\n')
sum = 0
for __ in _:
  sum+=int(__)
print(sum)