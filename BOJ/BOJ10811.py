N,M = map(int,input().split())

list_ = [i for i in range(1,N+1)]

for i in range(M):
    a,b = map(int,input().split())
    X = list_[a-1:b]
    X.reverse()
    list_[a-1:b] = X

for i in range(N):
    print(list_[i],end=' ')