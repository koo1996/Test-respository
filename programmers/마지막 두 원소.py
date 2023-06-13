def solution(num_list):
    a = len(num_list)
    if num_list[a-1] > num_list[a-2]:
        num_list.append(num_list[a-1] - num_list[a-2])
    else:
        num_list.append(num_list[a-1] * 2)
    return num_list

## 한줄 코딩
def solution(n):
    n.append(n[-1]-n[-2] if n[-1] > n[-2] else n[-1] * 2)
    return n