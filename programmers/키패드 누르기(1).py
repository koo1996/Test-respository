def solution(numbers, hand):
    dic_ = {1: [0,0], 2: [0,1], 3: [0,2],
             4: [1,0], 5: [1,1], 6: [1,2],
             7: [2,0], 8: [2,1], 9: [2,2],
             '*': [3,0], 0: [3,1], '#': [3,2]}
    answer = ''
    lefthand = dic_['*']
    righthand = dic_['#']
    for i in numbers:
        now = dic_[i]
        if i in [1,4,7]:
            lefthand = now
            answer += "L"
        elif i in [3,6,9]:
            righthand = now
            answer += "R"
        else:
            left_d = abs(now[0] - lefthand[0]) + abs(now[1] - lefthand[1])
            right_d = abs(now[0] - righthand[0]) + abs(now[1] - righthand[1])
            if left_d < right_d:
                lefthand = now
                answer += "L"
            elif left_d > right_d:
                righthand = now
                answer += "R"
            else:
                if hand == "right":
                    righthand = now
                    answer += "R"
                else:
                    lefthand = now
                    answer += "L"
    return answer