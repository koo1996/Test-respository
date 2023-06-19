def solution(n, m, section):
    answer = 0
    while section:
        p = section[0] + m
        while section and section[0] < p:
            section.pop(0)
        answer += 1
    return answer