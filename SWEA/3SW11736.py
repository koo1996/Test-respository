T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    qu = list(map(int,input().split()))
    for i in range(1,len(qu)-1): # 시작과 끝을 제외한 숫자중에
        if qu[i] > qu[i-1] and qu[i] < qu[i+1]: # 중간값에 해당하는 숫자가 있다면 cnt 1씩 증가
            cnt += 1
        elif qu[i] < qu[i-1] and qu[i] > qu[i+1]:
            cnt += 1
    print(f'#{tc} {cnt}')