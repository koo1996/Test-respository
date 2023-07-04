def solution(d, budget):
    answer = 0
    all_ = sum(d)
    d.sort(reverse = True)
    for i in d:
        if all_ <= budget:
            return len(d)
        if all_ - i > budget:
            all_ -= i
            answer += 1
        else:
            answer += 1
            break

    return len(d) - answer