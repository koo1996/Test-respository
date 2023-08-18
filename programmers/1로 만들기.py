def solution(num_list):
    n = 0
    for i in num_list:
        while i > 1:
            if i % 2:
                i = (i - 1) / 2
                n += 1
            else:
                i = i / 2
                n += 1
    return n