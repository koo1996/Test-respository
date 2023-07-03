def solution(lottos, win_nums):
    rank = [6,5,4,3,2,1,0]
    answer = []
    No_ = 0
    cnt = 0
    for i in lottos:
        if i == 0:
            No_ += 1
        else:
            if i in win_nums:
                cnt += 1   
    if cnt + No_:
        answer.append(rank.index(cnt+No_)+1)
    else:
        answer.append(6)

    if rank.index(cnt) > 4:
        answer.append(6)
    else:
        answer.append(rank.index(cnt)+1)
    return answer

# def solution(lottos, win_nums):

#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]