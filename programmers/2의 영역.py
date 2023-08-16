def solution(arr):
    cnt_ = []
    for i in range(len(arr)):
        if arr[i] == 2:
            cnt_.append(i)
    if len(cnt_) >= 2:
        return arr[cnt_[0]:cnt_[-1]+1]
    elif len(cnt_) == 1:
        return [arr[cnt_[0]]]
    else:
        return [-1]