def solution(n, control):
    for test in control:
        if test == "w":
            n += 1
        elif test == "s":
            n -= 1
        elif test == "d":
            n += 10
        else:
            n -= 10

    return n