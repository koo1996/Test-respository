a,b = map(int,input().split())

sto = [i for i in range(1,a+1)]
x_ = 0
y_ = 0
for i in range(b):
    x,y = map(int,input().split())
    x_ = sto[x-1]
    y_ = sto[y-1]
    sto[y-1] = x_
    sto[x-1] = y_

result = ' '.join(str(s) for s in sto)
print(result)