def solution(n, lost, reserve):
    reserve_ = set(reserve) - set(lost) 
    lost_ = set(lost) - set(reserve) 

    for i in reserve_:
        if i-1 in lost_:
            lost_.remove(i-1)
        elif i+1 in lost_:
            lost_.remove(i+1)
    return n - len(lost_)