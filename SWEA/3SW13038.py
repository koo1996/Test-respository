T = int(input())

for tc in range(1,T+1):
    Day = int(input())
    Date = list(map(int,input().split()))
    cnt = 0
    cnt2 = 0
    while cnt < Day:
        # 특별 케이스 추가 => n일 = 2 / 0 1 0 0 0 1 1  => 답이 2 (5가 나오면 오답)
        for i in range(len(Date)):     
            if cnt == Day:
                break
            else:
                if Date[i] == 1:
                    cnt += 1
                if cnt > 0:
                    cnt2 += 1
                
    print(f'#{tc} {cnt2}')
    

    # cnt = 0
    # cnt = 1
    # for i in Date:
    #     if i == 1:
    #         cnt += 1
    # qu = (Day - 1) // cnt
    # res_ = (Day - 1) % cnt
    # for j in range(res_):

    # result = (qu * 7) + 1
    # print(f'#{tc} {result}') 