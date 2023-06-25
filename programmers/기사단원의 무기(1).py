def solution(number, limit, power):
    answer = 0        
    for i in range(1,number+1):
        cnt = 0
        for j in range(1,int(i**(1/2)+1)): # 범위를 제곱근으로 줄여야 시간초과가 안 뜬다.
            if i % j == 0:
                cnt += 1
                if j**2 != i:
                    cnt += 1 
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer

