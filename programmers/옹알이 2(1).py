def solution(babbling):
    answer = 0
    word_ = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in word_:
            if j * 2 not in i:
                if j in i:
                    i = i.replace(j," ")
        if i.strip() == "":
            answer += 1
    return answer