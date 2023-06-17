def solution(arr):
    stk = []
    i = 0
    j = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
        else:
            if stk[j] < arr[i]:
                stk.append(arr[i])
                i += 1
                j += 1
            elif stk[j] >= arr[i]:
                if j == 0:
                    stk.pop(j)
                else:
                    stk.pop(j)
                    j -= 1    
    return stk