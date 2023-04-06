T = int(input())

for tc in range(1,T+1):
    qu = list(input())
    answer = True 
    for i in qu:
        if qu.count(i) != 2: # 중복되는 2개의 숫자가 존재하지 않으면 answer을 false 변경 / 4개의 숫자중에 중복되는 2개의 숫자가 하나라도 없으면 조건에 만족하지 않는다.
            answer = False

    if answer == True: # answer 값에 맞게 출력
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')
