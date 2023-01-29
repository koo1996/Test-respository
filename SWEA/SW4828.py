T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    number_ = list(map(int,input().split()))

    result = max(number_) - min(number_)
    print('#{} {}'.format(test_case,result))
