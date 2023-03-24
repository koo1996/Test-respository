T = int(input())
list = []
for tc in range(1,T+1):
    a,b,c,d = map(int,input().split())
    result = min(b,d) - max(a,c) # 종료 시간에서는 작은 숫자(b,d) - 시작 시간에서는 큰 숫자(a,c)
    if result < 0: # 음수이면 0 출력
        answer = 0
    else:
        answer = result
    list.append(f'#{tc} {answer}') # 초과시간 오류로 인해 리스트에 출력값을 저장한 후에 한번에 출력

for i in list:
    print(i)