def solution(a, b, c, d):
    X = [a, b, c, d]
    counts = [X.count(i) for i in X]
    if max(counts) == 4:
        answer = a * 1111
    elif max(counts) == 3:
        p = X[counts.index(3)]
        q = X[counts.index(1)]
        answer = (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            if a == b:
                answer = (a + c) * abs(a - c)
            else:
                answer = (a + b) * abs(a - b)
        else:
            q = X[counts.index(2)]
            answer = (a * b * c * d) / q ** 2
    else:
        answer = min(X)

    return answer