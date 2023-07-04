def solution(n, m):
    answer = []
    answer2 = []
    for i in range(1,n+1):
        if n % i == 0 and m % i == 0:
            answer2.append(i)
    answer.append(max(answer2))        
    answer.append(n * (m / max(answer2)))
    return answer