T = int(input())

for tc in range(1,T+1): # 테스트케이스
    qu = input() 
    if qu.count('x') >= 8: # 게임을 15판중에 8판 이상 졌을때 이길 가능성이 없다고 봅니다 answer = 'NO'
        answer = 'NO'
    else:
        answer = 'YES'
    print(f'#{tc} {answer}') 