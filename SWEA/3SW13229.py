T = int(input())

dic_ = {'MON': 1, 'TUE' : 2, 'WED' : 3, 'THU' : 4,'FRI' : 5,'SAT' : 6,'SUN' : 7}

for tc in range(1,T+1):
    qu = input()
    if qu == 'SUN': # SUN 입력하면 7 출력
        answer = 7
    else:
        answer = 7 - dic_[qu] # 그 외에는 SUN (7로 가정)에서 해당요일 value 만큼 빼기
    print(f'#{tc} {answer}')