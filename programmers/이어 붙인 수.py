def solution(num_list):
    sum1 = ""
    sum2 = ""
    for i in num_list:
        if i % 2 == 1:
            sum1 += str(i)
        else:
            sum2 += str(i)
    return int(sum1) + int(sum2)