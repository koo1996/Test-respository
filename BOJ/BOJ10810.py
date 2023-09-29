a,b = map(int,input().split())

sto = [0 for i in range(a)]

for i in range(b):
    x,y,z = map(int,input().split())
    for j in range(x-1,y):
        sto[j] = z

result = ' '.join(str(s) for s in sto)
print(result)
