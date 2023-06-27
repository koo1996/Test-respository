def solution(a, b, n):
    answer = 0    
    while n >= a:
        X = (n // a) * b 
        Y = n % a
        answer += X
        n = X + Y

    return answer