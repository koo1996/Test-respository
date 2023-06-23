def solution(keymap, targets):
    answer1 = []
    for i in targets: 
        times = 0        
        for j in i: 
            min_time = 101
            answer = False
            for k in keymap:           
                if j in k:
                    min_time = min(k.index(j)+1,min_time)
                    answer = True
            if not answer:
                times = -1
                break                  
            times += min_time
        answer1.append(times)
    return answer1