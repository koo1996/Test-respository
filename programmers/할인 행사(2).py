def solution(want, number, discount):
    answer = 0
    want_ = {} # 살 것
    for i in range(len(want)):
         want_[want[i]] = number[i]

    for i in range(len(discount)-9):
        discount_ = {}
        for j in range(i,i+10): #할인 상품 정리
            if discount[j] in discount_:
                discount_[discount[j]] += 1
            else:
                discount_[discount[j]] = 1

        if want_ == discount_:
            answer += 1        
    return answer

# from collections import Counter
# collections 모듈의 Counter 클래스를 이용하면 9~14번째 코드를 줄일 수 있다. 