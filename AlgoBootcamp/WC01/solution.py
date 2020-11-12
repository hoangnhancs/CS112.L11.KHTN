time = None
with open('review.inp','r') as f:
    line = f.read()
    a,b,c = map(int,line.split(' '))
time = min(a,b,c)
with open('review.out','w') as f:
    f.write(time)