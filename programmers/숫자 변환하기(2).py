def solution(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)

    while dp:
        if y in dp: #y가 dp안에 있으면 answer return
            return answer
        else:
            y_ = set() #i+n, 2*i, 3*i 중에 y보다 작거나 같은 값들을 set에 저장
            for i in dp:
                if i+n <= y:
                    y_.add(i+n)
                if i*2 <= y:
                    y_.add(i*2)
                if i*3 <= y:
                    y_.add(i*3)
            dp = y_ #연산한 값들을 dp에 저장
            answer += 1 #answer 1씩 증가
    return -1