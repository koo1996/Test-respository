T = int(input())

for tc in range(1, T+1):
    N = int(input())
    for i in range(N):
        arr = list(map(int,input().split())) #행렬
        arr2 = [[0] * N for _ in range(N)] #90도 회전
        arr3 = [[0] * N for _ in range(N)] #180도 회전
        arr4 = [[0] * N for _ in range(N)] #270도 회전
        print(arr[0],arr2[0],arr3[0],arr4[0]) 
    
