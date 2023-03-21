T = int(input())

for tc in range(1,T+1):
    a,b = map(int,input().split())
    if a + b == 24: # a, b 합이 24면 0으로 출력
        answer = 0
    elif a + b > 24: # a, b 합이 24보다 크면 24를 뺀다
        answer = a + b - 24
    else: # a, b 합이 24보다 작으면 그대로 출력
        answer = a + b
    print(f'#{tc} {answer}') 