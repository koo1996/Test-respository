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