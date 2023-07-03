def solution(n):
    answer = ""
    while True:
        if n < 3:
            answer += str(n)
            break
        answer += str(n % 3)
        n = n // 3

    answer = answer[::-1]
    return sum([int(answer[i]) * (3 ** i) for i in range(len(answer))])