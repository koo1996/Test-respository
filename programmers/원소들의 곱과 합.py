def solution(num_list):
    answer = 1
    sum_ = 0
    for i in num_list:
        answer *= i
    sum_ = sum(num_list)*sum(num_list)
    if answer < sum_:
        return 1
    else:
        return 0