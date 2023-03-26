T = int(input())

for tc in range(1,T+1): # 테스트케이스 
    N = int(input())
    sum = 0 
    for i in range(N): # 갯수
        a,b = map(float,input().split()) # a,b 소수로 입력
        result = a * b # a * b => result에 저장
        sum += result # sum에 result 누적합
    print(f'#{tc} {sum}') 