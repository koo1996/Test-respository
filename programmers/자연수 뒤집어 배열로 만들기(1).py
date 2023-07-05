def solution(n):
    n = str(n)[::-1]
    return [int(n[i]) for i in range(len(n))]