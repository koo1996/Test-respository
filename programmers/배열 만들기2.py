def solution(l, r):
    a = list(range(l,r+1))
    b = []
    for i in range(len(a)): 
        c = str(a[i])
        answer = 0
        for j in range(len(c)):
            if c[j] == "5" or c[j] == "0":
                answer = 1
            else:
                answer = 0
                break
        if answer:
            b.append(int(c))
    if not b:
        b.append(-1)
    else:
        b.sort()
    return b

# a = []
# for num in range(1,100):
#     if not set(str(num)) - set(["5","0"]):
#         a.append(num)

# return a if a else [-1]