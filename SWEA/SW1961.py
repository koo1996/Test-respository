T = int(input())

for tc in range(1, T+1):
    N = int(input())   
    arr = [list(map(str,input().split())) for _ in range(N)] #행렬
    arr2 = [[0] * N for _ in range(N)] #90도 회전
    arr3 = [[0] * N for _ in range(N)] #180도 회전
    arr4 = [[0] * N for _ in range(N)] #270도 회전
    
    for i in range(N):
        for j in range(N):
            arr2[i][j] = arr[N-1-j][i]
            arr3[i][j] = arr[N-1-i][N-1-j]
            arr4[i][j] = arr[j][N-1-i]
    print(f'#{tc}')
    for a1,a2,a3 in zip(arr2,arr3,arr4):
        q1 = ''.join(a1)
        q2 = ''.join(a2)
        q3 = ''.join(a3)
        print("{} {} {}".format(q1,q2,q3))
