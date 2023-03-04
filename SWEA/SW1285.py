#1번 풀이

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int,input().split()))
    list_ = []
    for i in range(N):        
        result_ = N_list[i] - 0
        list_.append(abs(result_))
    small = min(list_)
    count_ = list_.count(small)
    print('#{} {} {}'.format(tc, small, count_))

# 2번 풀이
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int,input().split()))
    length = abs(N_list[0])
    result = 0
    for i in N_list:
        if length > abs(i):
            length = abs(i)        
    result += N_list.count(length)
    result += N_list.count(-1*length)
    print('#{} {} {}'.format(tc, length, result))