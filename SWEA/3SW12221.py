T = int(input())

for tc in range(1,T+1):
    a, b = map(int,input().split())
    if a >= 10 or b >= 10: # a가 10보다 크거나 b가 10보다 크면 -1출력
        answer = -1 
    else:
        answer = a * b # 그 외에는 곱셈
    print(f'#{tc} {answer}')