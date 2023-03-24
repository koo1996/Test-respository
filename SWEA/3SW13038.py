T = int(input())

for tc in range(1,T+1):
    Day = int(input())
    Date = list(map(int,input().split()))
    cnt = 0
    cnt2 = 0
    while cnt < Day:
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