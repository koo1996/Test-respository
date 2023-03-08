T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    number_ = 0
    matrix = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            number_ += 1
            matrix[i][j] = number_
    print(matrix)
    # print('#{} {}'.format(test_case,answer))