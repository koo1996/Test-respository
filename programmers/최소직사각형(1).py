def solution(sizes):
    sum_1 = 0
    sum_2 = 0
    for i,j in sizes:        
        if max(i,j) > sum_1:
            sum_1 = max(i,j)
        if min(i,j) > sum_2:
            sum_2 = min(i,j)

    return sum_1 * sum_2