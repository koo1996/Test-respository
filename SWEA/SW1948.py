T = int(input())

for test_case in range(1, T + 1):
    dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} #dic 월,일 저장
    a,b,c,d = map(int,input().split())
    answer = 0
    for i in range(a,c): 
        if a == i:
            answer += dic[i] - b + 1
        else:
            answer += dic[i]
    answer += d
    print('#{} {}'.format(test_case,answer))
