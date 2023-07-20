def solution(N, stages):
    No_ = []
    l = len(stages)
    for i in range(1,N+1):        
        cnt = 0
        for j in range(len(stages)):
            if i == stages[j]:
                cnt += 1
        if cnt == 0:
            No_.append(0)
        else:
             No_.append(cnt / l)
        l = l - cnt

    k = {key + 1 : value for key,value in enumerate(No_)} 
    
    return sorted(k, key = lambda x : k[x] ,reverse = True)