T = int(input())

for tc in range(1,T+1):
    qu = int(input())
    if qu % 3 == 0: # 나머지가 0이면 qu/3  몫을 출력
        answer = qu//3
    else:  # 나머지가 0이 아니면 qu/3 몫을 출력
        answer = qu//3
    print(f'#{tc} {answer}')